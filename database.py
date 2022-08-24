# TODO add functionality

import sqlite3
from termcolor import colored

# DATETIME, EVENT, PRIORITY(Low, Medium, High), CALENDER(School, Work, Personal),


class Database:

    

    def init(self):
        # creates database, and connection
        self.con = sqlite3.connect('calendar.db')
        self.cur = self.con.cursor()
        
        # creates table if it doesn't exist
        self.cur.execute("CREATE TABLE IF NOT EXISTS calender(month TEXT, day INTEGER, calender TEXT, event TEXT)")
        self.con.commit()
        
        print("passed")
        pass

    def add_event(self,month,day,calendar,event):
        self.con = sqlite3.connect('calendar.db')
        self.cur = self.con.cursor()

        self.month = month
        self.day = day
        self.event = event
        self.calendar = calendar

        try: 
            self.cur.execute("INSERT INTO calender VALUES('{}',{},'{}','{}')".format(self.month,self.day,self.calendar,self.event))
        except:
            print("Error")

        print(colored("Passed", 'red'))

    def del_event(self,month,day,calendar):

        pass

    def update_event():
        pass

    def print_event(self):
        print(colored("Month {}".format(self.month)), '\n')
        print(colored("Day {}".format(self.day)), '\n')
        print(colored("Event {}".format(self.event)), '\n')


test = Database()

# test.init() 

test.add_event("August",24,"School","IME 254")
test.print_event()
