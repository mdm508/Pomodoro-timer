**TO RUN PROGRAM PUT break_time.py, Times.db, stopwatch.py, time_sheet_2016.txt, tracker.py and README.txt into a file. Then run break_time.py using python3 or later.

break_time allows you to track how long you have worked on projects. You will find the following commands essential.

Commands
add 	- add a subject to database
remove 	- removes subject from database
set 	- sets subject (meaning you are able to track it)
command - lists all the possible commands
enter 	- allows you to enter a time manually without tracking
go 	- as long as a subject as set, starts time, hit enter to end timer

The timer is based on the pomodoro technique. If you study over 25 or more minutes, a small X will appear in the shell. 4 X's signal that it is time to take a break.
To adjust the lenght of pomodoro's or how many it takes to trigger a break, change the global variables inside of tracker.py

you have the option to result the days results of time tracking to a file. by default the file is 'time_sheet_2016'. To change this, change the global variable FILE_PATH inside
break_time.py




