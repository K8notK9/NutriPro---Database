import random
import pandas as pd
import wx
from MealPlanFrame import MealPlanFrame

class MealPlanFrameLogic(MealPlanFrame):
    def __init__(self, parent, meal_plan_manager):
        super().__init__(parent)

        self.meal_plan_manager = meal_plan_manager
        self.current_view = 'daily'

        self.food_dataset = pd.read_csv('Food_Nutrition_Dataset.csv')  # Load dataset into a DataFrame

        self.day_choice.SetItems(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
        self.day_choice.SetSelection(0)

        self.initialize_list_control()

        # Bind events
        self.day_choice.Bind(wx.EVT_CHOICE, self.on_day_selected)
        self.weekly_view_button.Bind(wx.EVT_BUTTON, self.toggle_view)
        self.generate_meal_plan_button1.Bind(wx.EVT_BUTTON, self.on_generate_random_meal_plan)
        self.add_food_button.Bind(wx.EVT_BUTTON, self.on_add_food)
        self.change_food_button.Bind(wx.EVT_BUTTON, self.on_change_food)
        self.remove_food_button.Bind(wx.EVT_BUTTON, self.on_remove_food)
        self.clear_meal_plan_button.Bind(wx.EVT_BUTTON, self.on_clear_meal_plan)
        self.back_to_main_menu.Bind(wx.EVT_BUTTON, self.on_back_to_main_menu)
        self.go_to_data_list.Bind(wx.EVT_BUTTON, self.on_go_to_data_list)

        self.update_meal_plan_display()

    def initialize_list_control(self):
        self.meal_plan_list.DeleteAllColumns()
        self.meal_plan_list.InsertColumn(0, "Day")
        self.meal_plan_list.InsertColumn(1, "Meal")
        self.meal_plan_list.InsertColumn(2, "Food")
        self.meal_plan_list.InsertColumn(3, "Calories")
        self.meal_plan_list.InsertColumn(4, "Protein (g)")
        self.meal_plan_list.InsertColumn(5, "Carbs (g)")
        self.meal_plan_list.InsertColumn(6, "Fat (g)")

    def on_day_selected(self, event):
        self.update_meal_plan_display()

    def toggle_view(self, event):
        self.current_view = 'weekly' if self.current_view == 'daily' else 'daily'
        self.weekly_view_button.SetLabel(
            "Switch to Daily View" if self.current_view == 'weekly' else "Switch to Weekly View")
        self.update_meal_plan_display()

    def update_meal_plan_display(self):
        self.meal_plan_list.DeleteAllItems()
        meal_plan = self.meal_plan_manager.get_meal_plan()
        if self.current_view == 'daily':
            day = self.day_choice.GetStringSelection()
            self.display_day(day, meal_plan[day])
        else:
            for day in meal_plan:
                self.display_day(day, meal_plan[day])
        self.update_nutrient_summary()

    def display_day(self, day, day_plan):
        for meal, foods in day_plan.items():
            for food in foods:
                index = self.meal_plan_list.InsertItem(self.meal_plan_list.GetItemCount(), day)
                self.meal_plan_list.SetItem(index, 1, meal)
                self.meal_plan_list.SetItem(index, 2, food['name'])
                self.meal_plan_list.SetItem(index, 3, str(food['calories']))
                self.meal_plan_list.SetItem(index, 4, str(food['protein']))
                self.meal_plan_list.SetItem(index, 5, str(food['carbs']))
                self.meal_plan_list.SetItem(index, 6, str(food['fat']))

    def update_nutrient_summary(self):
        meal_plan = self.meal_plan_manager.get_meal_plan()
        if self.current_view == 'daily':
            day = self.day_choice.GetStringSelection()
            total_calories = sum(float(food['calories']) for meal in meal_plan[day].values() for food in meal)
            total_protein = sum(float(food['protein']) for meal in meal_plan[day].values() for food in meal)
            total_carbs = sum(float(food['carbs']) for meal in meal_plan[day].values() for food in meal)
            total_fat = sum(float(food['fat']) for meal in meal_plan[day].values() for food in meal)
        else:
            total_calories = sum(
                float(food['calories']) for day in meal_plan.values() for meal in day.values() for food in meal)
            total_protein = sum(
                float(food['protein']) for day in meal_plan.values() for meal in day.values() for food in meal)
            total_carbs = sum(
                float(food['carbs']) for day in meal_plan.values() for meal in day.values() for food in meal)
            total_fat = sum(float(food['fat']) for day in meal_plan.values() for meal in day.values() for food in meal)

        summary = f"Total for the {'week' if self.current_view == 'weekly' else 'day'}: "
        summary += f"Calories: {total_calories:.0f}, Protein: {total_protein:.1f}g, Carbs: {total_carbs:.1f}g, Fat: {total_fat:.1f}g"
        self.nutrient_summary.SetLabel(summary)

    def on_generate_random_meal_plan(self, event):
        """ Generate a random well-balanced meal plan for the entire week. """
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        meals = ['Breakfast', 'Lunch', 'Dinner', 'Snack']

        # Clear the current meal plan
        self.meal_plan_manager.clear_meal_plan()

        # For each day and each meal, select random food items that form a balanced meal
        for day in days:
            for meal in meals:
                selected_foods = self.generate_balanced_meal()
                for food in selected_foods:
                    self.meal_plan_manager.add_food(day, meal, food)

        # Update the display after generating the meal plan for the entire week
        self.update_meal_plan_display()

    def generate_balanced_meal(self):
        """ Selects a random set of food items from the dataset that form a balanced meal. """
        # Set targets for calories, protein, carbs, and fat (these can be modified as needed)
        calorie_target = 600  # Example target for a meal
        protein_target = 30  # Grams
        carb_target = 50  # Grams
        fat_target = 20  # Grams

        selected_foods = []
        total_calories, total_protein, total_carbs, total_fat = 0, 0, 0, 0

        # Keywords to filter for whole/cooked meals
        keywords = ['cooked', 'baked', 'grilled', 'roasted', 'fried', 'stewed', 'braised']

        # Filter the dataset by checking if any of the keywords appear in the 'food' column
        potential_foods = self.food_dataset[
            self.food_dataset['food'].str.contains('|'.join(keywords), case=False, na=False)
        ]

        if potential_foods.empty:
            print("No cooked meals found in the dataset.")
            return selected_foods  # Return empty if no matches

        while total_calories < calorie_target:
            food = potential_foods.sample().iloc[0]  # Randomly select a food item from the filtered list
            total_calories += food['Caloric Value']
            total_protein += food['Protein']
            total_carbs += food['Carbohydrates']
            total_fat += food['Fat']

            selected_foods.append({
                'name': food['food'],
                'calories': food['Caloric Value'],
                'protein': food['Protein'],
                'carbs': food['Carbohydrates'],
                'fat': food['Fat']
            })

            # Break when nearing the calorie target
            if total_calories >= calorie_target and total_protein >= protein_target:
                break

        return selected_foods

    def on_add_food(self, event):
        dialog = FoodSearchDialogLogic(self)
        if dialog.ShowModal() == wx.ID_OK:
            food = dialog.get_selected_food()
            if food:
                day = self.day_choice.GetStringSelection()
                meal_dialog = wx.SingleChoiceDialog(self, "Choose a meal", "Add to Meal",
                                                    ['Breakfast', 'Lunch', 'Dinner', 'Snack'])
                if meal_dialog.ShowModal() == wx.ID_OK:
                    meal = meal_dialog.GetStringSelection()
                    self.meal_plan_manager.add_food(day, meal, food)
                    self.update_meal_plan_display()
                meal_dialog.Destroy()
        dialog.Destroy()

    def on_change_food(self, event):
        selected_item = self.meal_plan_list.GetFirstSelected()
        if selected_item != -1:
            day = self.meal_plan_list.GetItemText(selected_item, 0)
            meal = self.meal_plan_list.GetItemText(selected_item, 1)
            food_name = self.meal_plan_list.GetItemText(selected_item, 2)

            dialog = FoodSearchDialogLogic(self)
            if dialog.ShowModal() == wx.ID_OK:
                new_food = dialog.get_selected_food()
                if new_food:
                    self.meal_plan_manager.change_food(day, meal, food_name, new_food)
                    self.update_meal_plan_display()
            dialog.Destroy()

    def on_remove_food(self, event):
        selected_item = self.meal_plan_list.GetFirstSelected()
        if selected_item != -1:
            day = self.meal_plan_list.GetItemText(selected_item, 0)
            meal = self.meal_plan_list.GetItemText(selected_item, 1)
            food_name = self.meal_plan_list.GetItemText(selected_item, 2)
            self.meal_plan_manager.remove_food(day, meal, food_name)
            self.update_meal_plan_display()

    def on_clear_meal_plan(self, event):
        self.meal_plan_manager.clear_meal_plan()
        self.update_meal_plan_display()

    def on_go_to_data_list(self, event):
        self.Hide()
        wx.GetApp().show_dataset_list()

    def on_back_to_main_menu(self, event):
        self.Hide()
        wx.GetApp().main_frame.Show()

# This allows the file to be run standalone for testing
if __name__ == '__main__':
    app = wx.App(False)
    frame = MealPlanFrameLogic(None, MealPlanManager())
    frame.Show(True)
    app.MainLoop()