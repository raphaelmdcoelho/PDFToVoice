import pyttsx3 as sp
import PyPDF2 as pdf

pdfReader = pdf.PdfReader(open('file.pdf', 'rb'))
engine = sp.init()

for page_num in range(len(pdfReader.pages)):
    text = pdfReader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    
current_rate = engine.getProperty('rate')
print(f"Current rate of speech: {current_rate}")

new_rate = 100
engine.setProperty('rate', new_rate)

voices = engine.getProperty('voices')

for voice in voices:
    print(f"ID: {voice.id}, Language: {voice.languages}, Name: {voice.name}")

new_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', new_voice_id)

engine.save_to_file(clean_text, 'audio.mp3')
engine.runAndWait()

engine.stop()