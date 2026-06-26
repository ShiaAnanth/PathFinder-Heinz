import PyPDF2


with open('aim-student-handbook.pdf', 'rb') as pdf_file: #rb stands for read only and binary so that the file does not convert non text elements
    reader = PyPDF2.PdfReader(pdf_file)
    for page in reader.pages[2:]: #loops through every page in the reader starting from page 3
        new = (page.extract_text()) #extracts all the text from the page 
        clean_page =' '.join(new.split())  #in a new empty variable, it adds the extracted text and also removes the spacing in the characters
        print(clean_page) #prints cleaned version of all pages 




