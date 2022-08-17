# pip install tkinter
# pip install path
# pip install pyttsx3
# pip install pydub
# pip install PyPDF4
# pip install SpeechRecognition

# ^ ye install karo before running
#⬇️ complete reference
# https://pythongeeks.org/python-convert-pdf-text-to-audio-speech/




#Importing modules for Python Project to Convert PDF Text to Audio Speech
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

from path import Path
from PyPDF4.pdf import PdfFileReader , PdfFileWriter
import pyttsx3
from speech_recognition import Recognizer, AudioFile
from pydub import AudioSegment
import os
#Declaring global variables related to PDF to Speech conversion
global endPg ,startPg

#Function to open the PDF selected and read text from it
def read():
    path = filedialog.askopenfilename() #Get the path of the PDF based on the user's location selection
    pdfLoc = open(path, 'rb') #Opening the PDF
    pdfreader = PdfFileReader(pdfLoc) # Creating a PDF reader object for the opened PDF
    speaker = pyttsx3.init() #Initiating a speaker object

    start=startPg.get() # Getting the starting page number input
    end=endPg.get() # Getting the ending page number input

    #Reading all the pages from start to end page number
    for i in range(start,end+1):
        page = pdfreader.getPage(i) #Getting the page
        txt = page.extractText() #Extracting the text
        speaker.say(txt) #Getting the audio output of the text
        speaker.runAndWait() # Processing the voice commands



#Function to create a GUI and get required inputs for PDF to Audio Conversion
def pdf_to_audio():
    #Creating a window
    wn1 = Tk()
    wn1.title("PythonGeeks PDF to Audio converter")
    wn1.geometry('500x400')
    wn1.config(bg='snow3')

    start_pgNo = IntVar(wn1) #Variable to hold the starting page number
    end_pgNo = IntVar(wn1) #Variable to hold the ending page number

    Label(wn1, text='PythonGeeks PDF to Audio converter',
    fg='black', font=('Courier', 15)).place(x=60, y=10)


    Label(wn1, text='Enter the start and the end page to read. If you want to read a single \npage please enter the start page and enter the next page as the end page:', anchor="e", justify=LEFT).place(x=20, y=90)

    #Getting the input of starting page number to be spoken
    Label(wn1, text='Start Page No.:').place(x=100, y=140)


    startPg = Entry(wn1, width=20, textvariable=start_pgNo)
    startPg.place(x=100, y=170)

    #Getting the input of ending page number to be spoken
    Label(wn1, text='End Page No.:').place(x=250, y=140)


    endPg = Entry(wn1, width=20, textvariable=end_pgNo)
    endPg.place(x=250, y=170)

    #Button to select the PDF and get the audio input
    Label(wn1, text='Click the below button to Choose the pdf and start to Listen:').place(x=100, y=230)
    Button(wn1, text="Click Me", bg='ivory3',font=('Courier', 13),command=read).place(x=230, y=260)

    wn1.mainloop()



#Declaring global variable for PDF to Speech conversion
global pdfPath

#Function to update the PDF file with the text, both given as parameters
def write_text(filename, text):
    writer = PdfFileReader() #Creating a PDF writer object
    writer.addBlankPage(72, 72) #Creating a blank page
    pdf_path = Path(filename) #Getting the path of the PDF
    with pdf_path.open('ab') as output_file: #Opening the PDF
        writer.write(output_file) #saving the text in the writer object
        output_file.write(text) #writing the text in the PDF




#Function to convert audio into text
def convert():
    path = filedialog.askopenfilename() #Getting the location of the audio file
    audioLoc = open(path, 'rb') #Opening the audio file

    pdf_loc=pdfPath.get() #Getting the path of the PDF

    #Getting the name and extension of the audio file and checking if it is mp3 or wav
    audioFileName = os.path.basename(audioLoc).split('.')[0]
    audioFileExt = os.path.basename(audioLoc).split('.')[1]
    if audioFileExt != 'wav' and audioFileExt != 'mp3':
        messagebox.showerror('Error!', 'The format of the audio file should be either "wav" and "mp3".')

    #If mp3 file converting it into wav file
    if audioFileExt == 'mp3':
        audio_file = AudioSegment.from_file(Path(audioLoc), format='mp3')
        audio_file.export(f'{audioFileName}.wav', format='wav')
        source_file = f'{audioFileName}.wav'

    #Creating a recognizer object and converting the audio into text
    recog= Recognizer()
    with AudioFile(source_file) as source:
        recog.pause_threshold = 5
        speech = recog.record(source)
        text = recog.recognize_google(speech)
        write_text(pdf_loc, text)





#Function to create a GUI and get required inputs for Audio to PDF Conversion
def audio_to_pdf():
#Creating a window
    wn2= Tk()
    wn2.title("PythonGeeks Audio to PDF converter")
    wn2.geometry('500x400')
    wn2.config(bg='snow3')

    pdfPath = StringVar(wn2) #Variable to get the PDF path input

    Label(wn2, text='PythonGeeks Audio to PDF converter',
    fg='black', font=('Courier', 15)).place(x=60, y=10)

    #Getting the PDF path input
    Label(wn2, text='Enter the PDF File location where you want to save (with extension):').place(x=20, y=50)
    Entry(wn2, width=50,textvariable=pdfPath).place(x=20, y=90)

    Label(wn2, text='Choose the Audio File location that you want to read (.wav or .mp3 extensions only):',
    fg='black').place(x=20, y=130)

    #Button to select the audio file and do the conversion
    Button(wn2, text='Choose', bg='ivory3',font=('Courier', 13),
    command=convert).place(x=50, y=170)
    wn2.mainloop() #Runs the window till it is closed



#Creating the main window
wn = Tk()
wn.title("PythonGeeks PDF to Audio and Audio to PDF converter")
wn.geometry('700x300')
wn.config(bg='LightBlue1')

Label(wn, text='PythonGeeks PDF to Audio and Audio to PDF converter',
fg='black', font=('Courier', 15)).place(x=40, y=10)

#Button to convert PDF to Audio form
Button(wn, text="Convert PDF to Audio", bg='ivory3',font=('Courier', 15),
command=pdf_to_audio).place(x=230, y=80)

#Button to convert Audio to PDF form
Button(wn, text="Convert Audio to PDF", bg='ivory3',font=('Courier', 15),
command=audio_to_pdf).place(x=230, y=150)

#Runs the window till it is closed
wn.mainloop()