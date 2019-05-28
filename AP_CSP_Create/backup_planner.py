from __future__ import print_function 
import sys
import json                                                                     #https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
import time 
import calendar as cal                                                          # https://docs.python.org/3/library/calendar.html#module-calendar
from datetime import datetime as dt                                             # https://docs.python.org/3/library/datetime.html#datetime.date.year 
# note: datetime is an object in the module datetime

''' Planner ''' 

now = dt.now()
today = dt.date(now)
year = now.year
month = now.month
day = now.day
weekday = cal.weekday(year, month, day)
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
days_of_month = range(1, 32)
months_of_year = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
to_do_list = []

class Task(object):
    '''
    Attributes: 
     - name: name of task
     - deadline: set by user 
     - day of deadline (mm/dd/yyyy)
     - month of deadline
     - year of deadline
    Methods: 
     - complete_task: marks task as completed, changes completed to True 
     - set_deadline: changes or sets deadline of a task 
    ''' 
    def __init__(self, name, deadline, day, month, year): 
        self.name = name
        self.deadline = deadline
        self.day = day
        self.month = month
        self.year = year

    def set_name(self, new_name):
        ''' Changes name of task ''' 
        self.name = new_name 
        
    def set_deadline(self, new_deadline):
        ''' Creates a due date for task ''' 
        self.deadline = new_deadline
    

def num_items_list():
    ''' States how many items are in the to-do list ''' 
    if len(to_do_list) != 1:
        print("You have", len(to_do_list), "items on your to-do list: ")
    else: 
        print("You have 1 item on your to-do list: ")
    time.sleep(1.5)


def print_list():
    '''
    Prints the to-do list in order of urgency (determined by due date)
    ''' 
    ordered_list = to_do_list
    ordered_list.sort()
    for item in ordered_list: 
        print(" ", item.name+",", "due", item.deadline)
        time.sleep(0.75) 

    
def interact_planner():
    '''
    Allows user to edit planner by adding assignments or completing 
        (separate function for completion?)
    Also allows deleting 
    '''
    print("What would you like to do now?")
    time.sleep(1)
    print(" 1) Complete a task")
    time.sleep(0.25)
    print(" 2) Edit your planner")
    time.sleep(0.25)
    print(" 3) Display your tasks")
    time.sleep(0.25)
    print(" 4) Exit the planner")
    time.sleep(1)
    next_action = raw_input("Choose a number: ")
    print()
    if next_action == "1":
        # Remove a task off to-do list after completing it 
        print_list()
        completed_task = raw_input("Which task have you completed? ")
        for item in to_do_list:
            if item.name == completed_task:
                to_do_list.remove(item)
                print("Congratulations on completing your assignment! That's one less thing on your to-do list :)")
    elif next_action == "2":
        # Edit planner: add new or edit existing 
        print("Options for editing: \n 1) Add a new assignment \n 2) Edit existing assignment")
        edit_choice = raw_input("Choose a number: ")
        if edit_choice == "1":
            # Add a new task 
            # using new_task = same variable?? 
            new_task = raw_input("Name your task: ")
            deadline = raw_input("When is your deadline (in the form of mm/dd/yyyy)? ")
            new_task = Task(new_task, deadline, int(deadline[3:5]), int(deadline[:2]), int(deadline[6:]))
            to_do_list.append(new_task)
            print("'"+new_task.name+"'", "has been successfully added to your planner :)")
        elif edit_choice == "2": 
            # Edit pre-existing task 
            print_list()
            print("Select a task to edit: ")
            task_to_edit = raw_input()
            for item in to_do_list:
                if item.name == task_to_edit:
                    new_name = raw_input("Change task name to: ")
                    new_deadline = raw_input("Change deadline to: ")
                    item.set_name(new_name)
                    item.set_deadline(new_deadline)
                    print("Your task has been successfully edited and saved.")
                # else: 
                #     print("Not an existing task.")
    elif next_action == "3":
        # Prints the to-do list again 
        num_items_list()
        print_list()
    elif next_action =="4":
        # Exits the program, asks if they would like to save? 
        save = raw_input("Would you like to save your planner before leaving? ")
        if save == "yes":
            saved_tasks = {}
            for number in range(1, len(to_do_list)+1):
                saved_tasks[number] = [to_do_list[number-1].name, to_do_list[number-1].deadline]
            with open("planner.txt", "w") as outfile:
                json.dump(saved_tasks, outfile)
            # planner_file = open("planner.txt", "w+")
            # for item in to_do_list:
            #     planner_file.write(item.name)
            # planner_file.close()
            print("Your to-do list has been successfully saved as planner.txt. Have a productive day!")
            sys.exit()
        elif save == "no":
            print("Goodbye! Hope you have a productive day :)")
            sys.exit() 
        else:
            print("Please type 'yes' or 'no' here.")
    else: 
        print("Please type a number to edit your planner.")
    print()
    interact_planner()


def default(): 
    ''' 
    Prints: 
        - inspirational message
        - date 
        - today's assignments, in order of urgency 
        - prompt on what to do 
    ''' 
    print("Welcome to your own personalized planner!")
    time.sleep(1)
    print("Today is", days_of_week[weekday]+",", months_of_year[month-1],str(days_of_month[day-1])+",", year, end=". \n")
    pre_saved = raw_input("Do you have a to-do list from using this planner before? ")
    if pre_saved == "yes":
        # planner_file = open("planner.text", "r+")
        # prev_tasks = planner_file.read()
        # for task in prev_tasks: 
        #     to_do_list.append(task)
        with open("planner.txt") as json_file:  
            saved_tasks = json.load(json_file)
            for key in saved_tasks:
                saved_task = Task("name", "deadline", "day", "month", "year")
                saved_task.set_name(saved_tasks[key][0])
                saved_task.set_deadline(saved_tasks[key][1])
                saved_task.day = int(saved_task.deadline[3:5])
                saved_task.month = int(saved_task.deadline[:2])
                saved_task.year = int(saved_task.deadline[6:])
                to_do_list.append(saved_task)
        print("Your previous planner has been successfully loaded from the file planner.txt")
    else: 
        time.sleep(0.5)
        num_items_list()
        print_list()
        print()
    interact_planner() 

''' ''' ''' ''' ''' '''

default() 



''' 
notes from running 
- annoying to display choices after "what would u like to do now" every time 
- inconsistency between formatting for "choose a number" 
- how to "press key for options" 
- arrange by due date, due date countdown feature 
- check consistency in time.sleep
- add inline comments 
- try except file no exist
''' 