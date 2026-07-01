import os
import pymupdf4llm



dir_path = "data"
out_path = "output"
os.makedirs(out_path, exist_ok=True)  # makes the output path the variable "out_path" and does not crash if folder already exists on second run


for handbooks in os.scandir(dir_path): #os library
    if handbooks.name.endswith(".pdf"):
            hb_md = pymupdf4llm.to_markdown(handbooks.path)  # extracts the markdown text from the handbooks original folder and stores it in variable new_hb_md
            program_name = handbooks.name.replace(".pdf", "") #stores the name of the hanbook into a variable by removing the .pdf from the end of its file name
            new_hb = os.path.join(out_path, f"{program_name}.md") #adds a new .md file to our output directory
            with open(new_hb,"w", encoding="utf-8") as newfile: #opens the new_hb file created in the output directory as newfile to write in it
                 newfile.write(hb_md) #writes the extracted markdown from the current handbook 
            