import logging
import threading
import time


import scheduler
from config import(clear,user)
from database import (Database)
from termcolor import colored

database = Database()

def main():
    clear()
    print(colored("\nHello {}, welcome to your personalized commandline Calender".format(user), 'cyan'))

    # TODO: add schedule type
    # create a scheduler object
    scheduler_obj = scheduler.Scheduler()

    print(colored("\nA scheduler object has been created. Would you like to edit it? (y/n)", 'green'))
    edit_scheduler = input()

    if edit_scheduler == "y":
        clear()
        event = input(colored("What would you like to add to your calender: ", 'yellow'))
        month = input(colored("What month is this scheduled for?: ", 'yellow'))
        day = input(colored("What day would you like to plan an event on?: ", 'yellow'))
            
        db = database.add_event(month, day, event)
        db.print_event()

            










def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    main()
    # format = "%(asctime)s: %(message)s"
    # logging.basicConfig(format=format, level=logging.INFO,
    #                     datefmt="%H:%M:%S")

    # threads = list()
    # for index in range(3):
    #     logging.info("Main    : create and start thread %d.", index+1)
    #     x = threading.Thread(target=thread_function, args=(index,))
    #     threads.append(x)
    #     x.start()

    # for index, thread in enumerate(threads):
    #     logging.info("Main    : before joining thread %d.", index+1)
    #     thread.join()
    #     logging.info("Main    : thread %d done", index+1)


