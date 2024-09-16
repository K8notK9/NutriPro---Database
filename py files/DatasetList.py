# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class DatassetList
###########################################################################

class DatassetList(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Search and Food Comparison", pos=wx.DefaultPosition,
                          size=wx.Size(1729, 1102), style=wx.DEFAULT_FRAME_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(153, 180, 209))

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        bSizer10 = wx.BoxSizer(wx.HORIZONTAL)

        self.search_label = wx.StaticText(self, wx.ID_ANY, u"Search:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.search_label.Wrap(0)
        bSizer10.Add(self.search_label, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.search_input = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.search_input.SetMaxLength(0)
        bSizer10.Add(self.search_input, 1, wx.ALL | wx.EXPAND, 5)

        self.search_button = wx.Button(self, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0)
        self.search_button.SetDefault()
        self.search_button.SetForegroundColour(wx.Colour(244, 247, 252))
        self.search_button.SetBackgroundColour(wx.Colour(0, 120, 215))

        bSizer10.Add(self.search_button, 0, wx.ALL, 5)

        bSizer9.Add(bSizer10, 0, wx.ALL | wx.EXPAND, 5)

        self.food_list = wx.ListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(880, 350),
                                     wx.LC_REPORT | wx.LC_SINGLE_SEL)
        bSizer9.Add(self.food_list, 1, wx.ALL | wx.EXPAND, 5)

        sbSizer5 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Filters"), wx.HORIZONTAL)

        self.filter_protein = wx.CheckBox(sbSizer5.GetStaticBox(), wx.ID_ANY, u"High Protein", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.filter_protein.SetValue(True)
        sbSizer5.Add(self.filter_protein, 1, wx.ALL, 5)

        self.filter_carbs = wx.CheckBox(sbSizer5.GetStaticBox(), wx.ID_ANY, u"Low Carbs", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.filter_carbs.SetValue(True)
        sbSizer5.Add(self.filter_carbs, 1, wx.ALL, 5)

        self.filter_fat = wx.CheckBox(sbSizer5.GetStaticBox(), wx.ID_ANY, u"Low Fat", wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        self.filter_fat.SetValue(True)
        sbSizer5.Add(self.filter_fat, 1, wx.ALL, 5)

        self.apply_filters = wx.Button(sbSizer5.GetStaticBox(), wx.ID_ANY, u"Apply Filters", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.apply_filters.SetDefault()
        self.apply_filters.SetForegroundColour(wx.Colour(244, 247, 252))
        self.apply_filters.SetBackgroundColour(wx.Colour(0, 120, 215))

        sbSizer5.Add(self.apply_filters, 0, wx.ALL, 5)

        bSizer9.Add(sbSizer5, 0, wx.ALL | wx.EXPAND, 5)

        sbSizer6 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Comparison"), wx.VERTICAL)

        self.comparison_list = wx.ListCtrl(sbSizer6.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size(880, 100),
                                           wx.LC_REPORT | wx.LC_SINGLE_SEL)
        sbSizer6.Add(self.comparison_list, 1, wx.ALL | wx.EXPAND, 5)

        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)

        self.generate_comparison_chart = wx.Button(sbSizer6.GetStaticBox(), wx.ID_ANY, u"Generate Comparison Chart",
                                                   wx.DefaultPosition, wx.DefaultSize, 0)
        self.generate_comparison_chart.SetDefault()
        self.generate_comparison_chart.SetForegroundColour(wx.Colour(244, 247, 252))
        self.generate_comparison_chart.SetBackgroundColour(wx.Colour(0, 120, 215))

        bSizer11.Add(self.generate_comparison_chart, 1, wx.ALL | wx.EXPAND, 5)

        self.clear_comparison = wx.Button(sbSizer6.GetStaticBox(), wx.ID_ANY, u"Clear Comparison", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.clear_comparison.SetDefault()
        self.clear_comparison.SetForegroundColour(wx.Colour(244, 247, 252))
        self.clear_comparison.SetBackgroundColour(wx.Colour(0, 120, 215))

        bSizer11.Add(self.clear_comparison, 1, wx.ALL | wx.EXPAND, 5)

        sbSizer6.Add(bSizer11, 0, wx.ALL | wx.EXPAND, 5)

        bSizer9.Add(sbSizer6, 0, wx.ALL | wx.EXPAND, 5)

        sbSizer7 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Meal Plan Options"), wx.HORIZONTAL)

        self.meal_plan_breakfast = wx.RadioButton(sbSizer7.GetStaticBox(), wx.ID_ANY, u"Breakfast", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
        self.meal_plan_breakfast.SetValue(True)
        sbSizer7.Add(self.meal_plan_breakfast, 1, wx.ALL, 5)

        self.meal_plan_lunch = wx.RadioButton(sbSizer7.GetStaticBox(), wx.ID_ANY, u"Lunch", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.meal_plan_lunch.SetValue(True)
        sbSizer7.Add(self.meal_plan_lunch, 1, wx.ALL, 5)

        self.meal_plan_dinner = wx.RadioButton(sbSizer7.GetStaticBox(), wx.ID_ANY, u"Dinner", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.meal_plan_dinner.SetValue(True)
        sbSizer7.Add(self.meal_plan_dinner, 1, wx.ALL, 5)

        self.meal_plan_snack = wx.RadioButton(sbSizer7.GetStaticBox(), wx.ID_ANY, u"Snack", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.meal_plan_snack.SetValue(True)
        sbSizer7.Add(self.meal_plan_snack, 1, wx.ALL, 5)

        self.add_to_meal_plan = wx.Button(sbSizer7.GetStaticBox(), wx.ID_ANY, u"Add to Meal Plan", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.add_to_meal_plan.SetDefault()
        self.add_to_meal_plan.SetForegroundColour(wx.Colour(244, 247, 252))
        self.add_to_meal_plan.SetBackgroundColour(wx.Colour(0, 120, 215))

        sbSizer7.Add(self.add_to_meal_plan, 0, wx.ALL, 5)

        bSizer9.Add(sbSizer7, 0, wx.ALL | wx.EXPAND, 5)

        self.go_to_meal_plan = wx.Button(self, wx.ID_ANY, u"Go to Meal Plan", wx.DefaultPosition, wx.DefaultSize, 0)
        self.go_to_meal_plan.SetDefault()
        self.go_to_meal_plan.SetForegroundColour(wx.Colour(244, 247, 252))
        self.go_to_meal_plan.SetBackgroundColour(wx.Colour(0, 120, 215))

        bSizer9.Add(self.go_to_meal_plan, 0, wx.ALIGN_RIGHT | wx.ALL | wx.EXPAND, 5)

        self.back_to_main_menu1 = wx.Button(self, wx.ID_ANY, u"Back to Main Menu", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.back_to_main_menu1.SetDefault()
        self.back_to_main_menu1.SetForegroundColour(wx.Colour(244, 247, 252))
        self.back_to_main_menu1.SetBackgroundColour(wx.Colour(0, 120, 215))

        bSizer9.Add(self.back_to_main_menu1, 0, wx.ALIGN_LEFT | wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer9)
        self.Layout()

    def __del__(self):
        pass


