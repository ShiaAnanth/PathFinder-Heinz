import pypdf
import os


dir_path = 'data'

'''
for entry in os.scandir(dir_path):  
    if entry.is_file():  # check if it's a file
        print(entry.path)
        '''

for file in os.scandir(dir_path):
    if file.name.endswith(".pdf"):
        with open(file, 'rb') as pdf_file: #rb stands for read only and binary so that the file does not convert non text elements
                
            reader = pypdf.PdfReader(pdf_file)
            for page in reader.pages[2:3]: #loops through every page in the reader starting from page 3
                new = (page.extract_text()) #extracts all the text from the page 
                clean_page =' '.join(new.split())  #in a new empty variable, it adds the extracted text and also removes the spacing in the characters
                print(clean_page) #prints cleaned version of all pages 





