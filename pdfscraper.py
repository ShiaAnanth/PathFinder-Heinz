import pypdf
import os
import json


dir_path = 'data'

handbook_texts = {}
for file in os.scandir(dir_path): #os library
    if file.name.endswith(".pdf"):
        program_name = file.name.replace('.pdf', '').split('-')[0].upper()
        with open(file, 'rb') as pdf_file: #rb stands for read only and binary so that the file does not convert non text elements
                
            reader = pypdf.PdfReader(pdf_file)
            full_text = ""
            for page in reader.pages: #loops through every page in the reader starting from page 3
                new = (page.extract_text()) #extracts all the text from the page 
                clean_page =' '.join(new.split())  #in a new empty variable, it adds the extracted text and also removes the spacing in the characters
                full_text += " " + clean_page
                
            handbook_texts[program_name] = full_text  # store in dictionary
            
# after the loop, print to verify it worked
#for name, text in handbook_texts.items(): #looks through all keys in dictionary
    #print(f"{name}: {text[:100]}")  # print first 100 chars of each

# Save to file
with open("handbooks.json", "w", encoding='utf-8') as hb_files:
    json.dump(handbook_texts, hb_files, indent=4, sort_keys=True, ensure_ascii=False)





