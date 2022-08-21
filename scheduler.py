# this is a weekly calender for the schedules

import time
from datetime import date

today = date.today()

class Scheduler:

    def __init__(self):
        self.schedules = {}
        self.schedules['Monday'] = []
        self.schedules['Tuesday'] = []
        self.schedules['Wednesday'] = []
        self.schedules['Thursday'] = []
        self.schedules['Friday'] = []
        self.schedules['Saturday'] = []
        self.schedules['Sunday'] = []

    def add_schedule(self, day, schedule):
        self.schedules[day].append(schedule)

    def delete_schedule(self, day, schedule):
        self.schedules[day].remove(schedule)   

    def get_schedule(self, day):
        return self.schedules[day]
    
    def set_schedule(self, day, schedule):
        self.schedules[day] = schedule

    def get_schedules(self):
        return self.schedules

