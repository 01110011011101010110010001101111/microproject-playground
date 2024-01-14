from pdfminer.high_level import extract_text

# params
READ_PDF = False
PDF_NAME = "campbell_original"

if READ_PDF: 
    # if haven't yet read the pdf, use pdfminer to extract text
    pdf_text = extract_text(f'{PDF_NAME}.pdf')

    # write to txt file
    with open(f"{PDF_NAME}.txt", "w") as text_file:
        text_file.write(pdf_text)
else:
    # if already read the pdf, read the txt file
    with open(f"{PDF_NAME}.txt","r") as f:
        pdf_text = f.read()

# print results
print("PDF_TO_TEXT_RESULT")
print(pdf_text)
print("END_PDF_TO_TEXT_RESULT")

## STEP 2: convert to audio file (with gTTS)
from gtts import gTTS

def text_to_audio(text, audio_file_path):
    tts = gTTS(text=text, lang='en')
    tts.save(audio_file_path)

output_audio_path = f'{PDF_NAME}.mp3'
text_to_audio(pdf_text, output_audio_path)

