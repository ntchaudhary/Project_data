import speech_recognition as sr 

#creating an instance for Microphone class
mic=sr.Microphone()

#Initialize the recognizer 
r = sr.Recognizer() 

print("this will take input from mic")
#use the microphone as source for input.  
with mic as source: 
	#wait for a second to let the recognizer adjust the 
	#energy threshold based on the surrounding noise level 
	r.adjust_for_ambient_noise(source) 
	print ("Say Something")
	#listens for the user's input 
	audio = r.listen(source) 
		
	try: 
		text = r.recognize_google(audio) 
		print ("you said: " + text) 
	
	#error occurs when google could not understand what was said 
	
	except sr.UnknownValueError: 
		print("Google Speech Recognition could not understand audio") 
	
	except sr.RequestError as e: 
		print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
