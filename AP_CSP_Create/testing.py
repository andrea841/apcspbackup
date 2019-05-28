from __future__ import print_function 
import calendar as cal
from datetime import datetime as dt 
import json 
# note: datetime is an object in the module datetime

# now = dt.now()
# today = dt.date(now)
# year = dt.year(now)
# month = dt.month(now)
# day = dt.day(now)
# weekday = cal.weekday(year, month, day)
to_do_list = []

# class Task(object):
#     '''
#     Attributes: 
#      - deadline: set by user 
#      - completed: False 
#     Methods: 
#      - complete_task: marks task as completed, changes completed to True 
#      - set_deadline: changes or sets deadline of a task 
#     ''' 
#     def __init__(self, name, deadline, completed=False): 
#         self.name = name
#         self.deadline = deadline
#         self.completed = completed 
        
#     def set_name(self, new_name):
#         ''' Changes name of task ''' 
#         self.name = new_name 
    
#     def complete_task(self): 
#         ''' Marks task as completed ''' 
#         self.completed = True
        
#     def set_deadline(self, new_deadline):
#         ''' Creates a due date for task ''' 
#         self.deadline = new_deadline

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

# new_task = raw_input("Name your task: ")
# deadline = raw_input("When is your deadline? ")
# new_task = Task(new_task, deadline)
# to_do_list.append(new_task)
# print("'"+new_task.name+"'", "has been successfully added to your planner :)")


# file = open("planner.txt", "r+")
# # print(file.read())
# # print("Next: ")
# # print(file.readline())
# stripped_lines = file.rstrip()
# print(file.readlines())
# file.close()

# list1 = []
# file = open("planner.txt", "r+")
# for line in file:
#     #print(line)
#     list1.append(line.rstrip('\n'))
    
# list2 = [x for x in range(1, len(list1)) if x % 2 != 0]
# list3 = []
# for index in list2: 
#     file.seek(0)
#     new_object = Task("name", "deadline")
#     print(new_object.name)
#     new_object.set_name(file.readline(index))
#     print(new_object.name)
#     new_object.set_deadline(file.readline(index+1))
#     print(new_object.deadline)
#     list3.append(new_object)


# ''' 
# data = {}  
# data['people'] = []  
# data['people'].append({  
#     'name': 'Scott',
#     'website': 'stackabuse.com',
#     'from': 'Nebraska'
# })
# data['people'].append({  
#     'name': 'Larry',
#     'website': 'google.com',
#     'from': 'Michigan'
# })
# data['people'].append({  
#     'name': 'Tim',
#     'website': 'apple.com',
#     'from': 'Alabama'
# })

# with open('data.txt', 'w') as outfile:  
#     json.dump(data, outfile)
# ''' 


# print(list3)
# print(file.readline(1))
# print(file.readline(2))
# print(file.readline(3))
# print(file.readline(4))
# print(file.readline(5))

# file.close() 


''' json ''' 

# saved_tasks = {}
# to_do_list = ["AP CSP", "AP Physics", "AP Chinese"]
# for number in range(1, len(to_do_list)):
#     saved_tasks[number] = [to_do_list[number-1]]
# with open("planner.txt", "w") as outfile:
#     json.dump(saved_tasks, outfile)
    

# with open('planner.txt') as json_file:  
#     prev_planner = json.load(json_file)
#     print(prev_planner)
    
task1 = Task("1", "04/15/2019", "04", "15", "2019")
task2 = Task("2", "03/15/2019", "03", "15", "2019")
task3 = Task("3", "04/14/2019", "04", "14", "2019")
to_do_list = [task1, task2, task3]
ordered_list = []
for item in to_do_list:
    ordered_list.append(item)
    ordered_list.sort(key = lambda item: (item.day, item.month, item.year))
for item in ordered_list:
    print(item.deadline)
# ordered_list = sorted(to_do_list, key=lambda x: (item.year, item.month, item.day) 