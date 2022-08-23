# TODO add functionality

import sqlite3

# DATETIME, EVENT, PRIORITY(Low, Medium, High), CALENDER(School, Work, Personal),


class Database:

    

    def init(self):
        # creates database, and connection
        self.con = sqlite3.connect('calendar.db')
        self.cur = self.con.cursor()
        
        # creates table if it doesn't exist
        self.cur.execute("CREATE TABLE IF NOT EXISTS events(id INTEGER PRIMARY KEY, month INTEGER, day INTEGER, event TEXT)")
        self.con.commit()
        
        print("passed")
        pass

    def add_event(self,month,day,event):
        self.month = month
        self.day = day
        self.event = event

    def del_event():
        pass

    def update_event():
        pass

    def print_event(self):
        print(colored("Month {}".format(self.month)), '\n')
        print(colored("Day {}".format(self.day)), '\n')
        print(colored("Event {}".format(self.event)), '\n')