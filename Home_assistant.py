import speech_recognition as sr
#print(sr.__version__)

# create instance of Recognizer
recognizer = sr.Recognizer()

# record signal
mic = sr.Microphone()
while(True):
	try:
		print("Say something!")
		with mic as source:
			# get audio from microphone
			audio = recognizer.listen(source)
			
			# extract text
			text = recognizer.recognize_google(audio)
			text = text.lower()
			if "return" in text:
				break
			elif "you" in text:
				print("I'm fine")
			else:
				print(text)
				if text.startswith("james"):
					print("I didnt get you")
	except KeyboardInterrupt:
		break
	except:
		print("Error")
