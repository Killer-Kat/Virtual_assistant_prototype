import pyttsx3
import speech_recognition as sr
#import webbrowser
import datetime
from datetime import date
from datetime import datetime
import wikipedia

#based on this https://www.geeksforgeeks.org/build-a-virtual-assistant-using-python/
#however the orignal code is very sloppy, this will require some cleaning up.

# this method is for taking the commands
# and recognizing the command from the
# speech_Recognition module we will use
# the recongizer method for recognizing
def takeCommand():

	r = sr.Recognizer()

	# from the speech_Recognition module
	# we will use the Microphone module
	# for listening the command
	with sr.Microphone() as source:
		print('Listening')
		
		# seconds of non-speaking audio before
		# a phrase is considered complete
		r.pause_threshold = 0.5
		audio = r.listen(source)
		
		# Now we will be using the try and catch
		# method so that if sound is recognized
		# it is good else we will have exception
		# handling
		try:
			print("Recognizing")
			
			# for Listening the command in indian
			# english we can also use 'hi-In'
			# for hindi recognizing
			Query = r.recognize_google(audio, language='en-US')
			print("the command is printed=", Query)
			
		except Exception as e:
			print(e)
			print("Say that again sir")
			return "None"
		
		return Query

def speak(audio):
	
	engine = pyttsx3.init()
	# getter method(gets the current value
	# of engine property)
	voices = engine.getProperty('voices')
	
	# setter method .[0]=male voice and
	# [1]=female voice in set Property.
	engine.setProperty('voice', voices[1].id)
	
	# Method for the speaking of the the assistant
	engine.say(audio)
	
	# Blocks while processing all the currently
	# queued commands
	engine.runAndWait()

def tellDay():
	
	# This function is for telling the
	# day of the week
	day = datetime.today().weekday() + 1
	today = date.today()
	d2 = today.strftime("%B %d, %Y")
	print("d2 =", d2)
	#this line tells us about the number
	# that will help us in telling the day
	Day_dict = {1: 'Monday', 2: 'Tuesday',
				3: 'Wednesday', 4: 'Thursday',
				5: 'Friday', 6: 'Saturday',
				7: 'Sunday'}
	
	if day in Day_dict.keys():
		day_of_the_week = Day_dict[day]
		print(day_of_the_week)
		speak("The day is " + day_of_the_week + " " + d2)


def tellTime():
	
	# This method will give the time
	time = datetime.now()

	# the time will be displayed like
	# this "2020-06-05 17:50:14.582630"
	#nd then after slicing we can get time
	print(time)
    
	speak("The time is " + time.strftime("%I:%M %p"))	

def SearchWiki(query):
	try:
		speak("Checking the wikipedia ")
		query = query.replace("wikipedia", "")
			
			# it will give the summary of 4 lines from
			# wikipedia we can increase and decrease
			# it also.
			
		result = wikipedia.summary(query, sentences=4)
		speak("According to wikipedia")
		speak(result)
	except Exception as e:
		print("ERROR: " + str(e))
		speak("An error has occured, unable to get wikipedia page " + query)


def Hello():
	
	# This function is for when the assistant
	# is called it will say hello and then
	# take query
	speak("hello sir I am your desktop assistant. Tell me how may I help you")


def Take_query():

	# calling the Hello function for
	# making it more interactive
	Hello()
	
	# This loop is infinite as it will take
	# our queries continuously until and unless
	# we do not say bye to exit or terminate
	# the program
	while(True):
		
		# taking the query and making it into
		# lower case so that most of the times
		# query matches and we get the perfect
		# output
		query = takeCommand().lower()
			
		if "what day is it" in query:
			tellDay()
			continue
		elif "tell me the date" in query:
			tellDay()
			continue
		elif "tell me the time" in query:
			tellTime()
			continue
		elif "what time is it" in query:
			tellTime()
			continue
		
		# this will exit and terminate the program
		elif "bye" in query:
			speak("Bye.")
			exit()
		
		elif "search wikipedia" in query:
			SearchWiki(query)
			continue
		
		elif "tell me your name" in query:
			speak("I am Jarvis. Your desk top Assistant")
			continue
		elif "what is your purpose" in query:
			speak("I pass butter. No wait I'm a prototype virtutal assistant.")
			continue

if __name__ == '__main__':
	
	# main method for executing
	# the functions
	Take_query()