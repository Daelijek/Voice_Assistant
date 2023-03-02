import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
	engine.say(text)
	engine.runAndWait()

def take_command():
	try:
		with sr.Microphone() as source:
			talk('Ara saka voice assistant greets you')
			talk('I am listening to you')
			print('Listening...')
			voice = listener.listen(source)
			command = listener.recognize_google(voice)
			command = command.lower()
			if 'arasaka' in command:
				command = command.replace('arasaka', '')
				print(command)
	except:
		pass
	return command
 
def run_arasaka():
	command = take_command()
	if 'play' in command:
		song = command.replace('play', '')
		talk('Playing' + song)
		pywhatkit.playonyt(song)
	elif 'time' in command:
		time = datetime.datetime.now().strftime('%H:%M')
		print(time)
		talk('Current time is ' + time)
	elif 'information' in command:
		person = command.replace('information', '')
		info = wikipedia.summary(person, 1)
		print(info)
		talk(info)
	elif 'are you single' in command:
		talk("I am in relationship with Wi-Fi")
		print('I am in relationship with Wi-Fi')
	elif 'date' in command:
		talk('Sorry, I have a headache')
		print('Sorry, I have a headache')
	else:
		talk('Please say the command again.')
		print('Please say the command again.')

while True:
	run_arasaka()