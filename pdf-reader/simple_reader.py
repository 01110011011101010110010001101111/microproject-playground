from pdfminer.high_level import extract_text

PDF_NAME = "campbell_original"
pdf_text = extract_text(f'{PDF_NAME}.pdf')

with open(f"{PDF_NAME}.txt", "w") as text_file:
    text_file.write(pdf_text)

print("PDF_TO_TEXT_RESULT")
print(pdf_text)
print("END_PDF_TO_TEXT_RESULT")

from gtts import gTTS

def text_to_audio(text, audio_file_path):
    tts = gTTS(text=text, lang='en')
    tts.save(audio_file_path)

output_audio_path = f'{PDF_NAME}.mp3'

text_to_audio(pdf_text, output_audio_path)

