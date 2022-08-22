# this is a weekly calender for the schedules

import time
from datetime import date

today = date.today()

class Scheduler:

    def __init__(self):
        self.days = 31
        self.weeks = 52
        self.months = 12
        
        
        self.schedules = {
            # this will allow the application to track what month, year, and number of days for that month
            'Datetime': {            
                'Month': [],
                'Year': 2022,
                'Days': 31,
            },

            'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': [],
            'Saturday': [],
            'Sunday': []
        }

        # self.schedules['Monday'] = []
        # self.schedules['Tuesday'] = []
        # self.schedules['Wednesday'] = []
        # self.schedules['Thursday'] = []
        # self.schedules['Friday'] = []
        # self.schedules['Saturday'] = []
        # self.schedules['Sunday'] = []

    def add_schedule(self, day, schedule):
        self.schedules[day].append(schedule)

    def delete_schedule(self, day, schedule):
        self.schedules[day].remove(schedule)   

    def get_todays_schedule(self, day):
        return self.schedules[day]

    def get_weeks_schedule(self):
        return self.schedules['Monday'] + self.schedules['Tuesday'] + self.schedules['Wednesday'] + self.schedules['Thursday'] + self.schedules['Friday'] + self.schedules['Saturday'] + self.schedules['Sunday']

        return self.schedules[week]
    
    def set_schedule(self, day, schedule):
        self.schedules[day] = schedule

    def get_schedules(self):
        return self.schedules

