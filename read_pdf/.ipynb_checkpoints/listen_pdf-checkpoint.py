#Importing necessary modules 
import pyttsx3
import PyPDF2

# Read the PDF file binary mode
pdf_file = open('sample.pdf', 'rb')
# print(pdf_file)

read_pdf = PyPDF2.PdfFileReader(pdf_file, strict=False)
# print(type(read_pdf))

#Find the number of pages in the PDF document
number_of_pages = read_pdf.getNumPages()
# print(type(number_of_pages))

engine = pyttsx3.init()
# print(type(engine))


# text = 'The quick brown fox jumped over the lazy dog.'
# engine.say(text)

page = read_pdf.getPage(0)
# print(type(page))
page_content = page.extractText()
print(type((page_content)))
# print(repr(page_content))


# setting audio properties
newrate=200
engine .setProperty('rate',newrate)
newvolume = 200
engine.setProperty('volume',newvolume)

# saying the output 
engine.say(page_content)
engine.runAndWait()



'''

for i in range(0, number_of_pages):

    # Read the pdf page
    page = read_pdf.getPage(i)

    # Extract the page from the pdf page
    page_content = page.extractText()
    
    #Set the audio speed and volume
    newrate = 200
    engine.setProperty('rate',newrate)
    newvolume = 200
    engine.setProperty('volume', newvolume)

    engine.say(page_content)

    #run and wait methods to processes the voice command
    engine.runAndWait()

'''




