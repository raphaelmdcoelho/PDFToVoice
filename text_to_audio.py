import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty("voices")[0] 
engine.setProperty('voice', voices)
text = 'Just a example'
engine.save_to_file(text, 'text.mp3')
engine.runAndWait()