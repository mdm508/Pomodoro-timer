from time import strftime
POMO_CHAR = 'X'
POMO_BREAK = 4
POMO_TIME = 20
#SHORT_BREAK = 90
#LONG_BREAK = 180
class tracker:
	def __init__(self):
		self._current = 0
		self._total = 0
		self._break_time = 0
		self._subjects = dict()
		self._pomos = 0
	def add_subject(self, subject, time=0):
		self._subjects[subject] = time
	def remove_subject(self, subject):
		'''assumes subject is a valid subject'''
		self._subjects.pop(subject)
	def get_current(self):
		return self._current
	def get_total(self):
		return self._total
	def get_breaks(self):
		return self._break_time
		
	def write(self, file_name,db):
	#if strftime("%w") == "0": #if its a sunday
		f = open(file_name, 'a')
		f.write("\n" + "--"*20)
		f.write("\nSUMMARY\n")
		f.write(strftime("\n%A, %B %d\n"))
		for subj, time in db.items():
			h,m = divmod(time,60)
			f.write(subj + ": " + str(h) + ' hours ' + str(m) + ' minutes \n')
		f.write("--"*20)
		f.close() 
	##      def write(self, file_name):
		
#               f = open(file_name, 'a')

#               f.write(strftime("\n%A, %B %d\n"))

#               for subject, time in self._subjects.items():
#                       hours, mins = divmod(time,60)
#                       f.write(subject + ': ' + str(hours) + ',' + 
#                                       str(mins) + '\n')
#               hours, mins = divmod(self._total, 60)
#               f.write("Total Time studied = " + str(hours) + ' hours ' +
#                                       str(mins) + ' minutes \n')
#               hours, mins = divmod(self._break_time, 60)
#               f.write("Total Breaks = " + str(hours) + " hours " + str(mins) + ' mins\n')
#               print(strftime("%w"))
	def inc_pomo(self):
		self._pomos +=1

	def display_pomos(self):
		s = ''
		for x in range(1, self._pomos + 1):
			if x % POMO_BREAK  == 0:
				s += POMO_CHAR + '-'
			else:
				s += POMO_CHAR
		print(s)
	def add(self, subject, time):
		#adds to subjects time`
		self._subjects[subject] += time
	
	def get_subjects(self):
		return self._subjects 

	def is_subject(self, subject)->bool:
		#checks if valid subject was given
		return subject in self._subjects

	def is_break(self,subject):
		return subject == "Break"
		
	def add_to_total(self, time):
		self._total += time

	def add_to_current(self,time):
		self._current +=time

	def add_to_break(self,time):
		self._break_time += time

	def reset_current(self):
		self._current = 0
