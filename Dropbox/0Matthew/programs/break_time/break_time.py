#!/usr/local/bin/python

#Author: Matthew McLaughlin
#Time for a break
#Determines if its time for a short break or a long break
#optionally write study progress to a file
from tracker import *
import shelve
import stopwatch
import re
#GLOBALS
pattern = "^[0]|[1-9][0-9]*$"
long_break = 180
short_break = 90
DASHES  = 60
FILE_NAME = "time_sheet_2016.txt"
message = "Enter Time: "
message2 = "Enter a subject to track: "
message3 = "Enter to stop, anything to peek: "
message4 = "Enter a command: "


def add_subject(tracker, data_base):
        '''add subject to dict and the database'''
        i  = input("Enter subject to add: ")
        tracker.add_subject(i)
        data_base[i] = 0

def is_valid_time(time):
        '''return if valid integer time is entered'''
        match = re.search(pattern, time)
        return match
        
def get_valid_time():
        '''ensures user input for time is correct'''
        time = input(message)
        while not is_valid_time(time) and time != 'q':
                print("Enter valid time")
                time = input(message)
                match = re.search(pattern,time)
        if time  == 'q': return 0
        return int(time)

def track_time(t:tracker, curr_subject):
        '''control the starting and stopping of the timer'''
        print("Time Started")
        timer = stopwatch.StopWatch()
        timer.start()
        x = input(message3)
        while x:
                print(timer.elapsed())
                x = input(message3)
        timer.stop()
        print(timer.elapsed())
        time = get_valid_time()
        if time != 'q' and time != 0:
                enter_time(t, curr_subject,time)     

def enter_time(t:tracker, curr_subject, time):
        '''this functions assumes time is valid'''
        t.add(curr_subject,time)
        t.add_to_total(time)
        t.add_to_current(time)
        if time >= POMO_TIME:
                t.inc_pomo()
                t.display_pomos()

def select_subject(tracker):
        '''select subject to track time for'''
        print_subjects(tracker)
        s = input(message2)
        while not tracker.is_subject(s):
                s = input("Enter valid subject: ")
        return s

def remove_subject(tracker, data_base):
        bold_message("Warning, once you remove a subject, there is no turning back")
        subject = input("Enter subjec to remove: ")
        if tracker.is_subject(subject):
                tracker.remove_subject(subject)
                data_base.pop(subject)
                print(subject, "removed")
        else:
                print("Either you entered an invalid subject or you: aborted")
                
def print_subjects(tracker):
        "Display currently being tracked"       
        for subject in tracker.get_subjects().keys():
                print(subject, end=  ', ')
        print()
        
def show_commands():
        '''displays a list of all the possible commands'''
        commands = "go", "add", "remove", 'set', 'subjects', 'commands'
        for c in commands:
                print(c,end=', ')
        print()

def write_to_console(tracker):
        '''writes total time studied to the console'''
        hours, minutes = divmod(tracker.get_total(),60)
        print("\nTotal hours:" , hours)
        print("Total minutes:", minutes)
        hours, minutes = divmod(tracker.get_breaks(),60)
        print("Total break time, hours = ", hours, "minutes = ", minutes,'\n')
        
def store_data(tracker, data_base):
        '''write data to the database and a file'''
        subjects = tracker.get_subjects()
        for key in sorted(subjects.keys()):
                data_base[key]+= subjects[key]
        tracker.write(FILE_NAME,data_base) 
        print("Wrote to --> ", FILE_NAME)
        print("-"*DASHES)

def bold_message(message):
        print("-"*DASHES)
        print(message)
        print("-"*DASHES)

def main():
        t = tracker()
        #add existing subjects into time tracker        
        db = shelve.open("Times",writeback=True)
        for subject in db:
                t.add_subject(subject)
        print()
        bold_message("Welcome to the time tracker.")
        c = input(message4)
        subject_set = False
        while c != 'q':
                if c == "go":
                        if subject_set:
                                track_time(t, selected_subject)
                        else:
                                bold_message("Subject not set")
                elif c == "add":
                        add_subject(t, db)
                elif c == "remove":
                        remove_subject(t, db)
                elif c == "set":
                        selected_subject = select_subject(t)
                        subject_set = True
                elif c == "subjects":
                        print_subjects(t)
                elif c == "commands":
                        show_commands()
                elif c == "enter":
                        if subject_set:
                                time = get_valid_time()
                                enter_time(t, selected_subject,time)
                        else:
                                bold_message("Subject not set")
                else:
                        print("not a valid command")
                c = input(message4)
        i = input("\nWould you like to store your data? y/n: ")
        if i != '' and i[0].upper() =='Y':
                store_data(t, db)
        write_to_console(t)
        db.close()
main()
'''
TO DO LIST
1. is doing input using dict possible
        commands = {    "go": track_time,
                        "add" : add_subject,
                        "remove": remove_subject,
                        "s": select_subject,
                   }
2. find out why break_time in track_time is treated not the same as a subject?
3. implement an "is break method" that retruns a bool as to wether or not it is time for a break
4. Make it possible to iterate directly over a tracker object
5. Make the output text able to write_to_console
by the way ctl+n is sweet!!
'''

