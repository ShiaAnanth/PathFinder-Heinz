from langchain_text_splitters import MarkdownHeaderTextSplitter , RecursiveCharacterTextSplitter
import re
import os

#loops through each of the documents in the folder 'output'
def main():
    all_chunks = [] #creates an empty list which will be passed onto chroma db
    dir_path = "output" 
    for handbook_md in os.scandir(dir_path): #goes through the handbook markdowns from the output directory with the cleaned md
        if handbook_md.name.endswith(".md"): #checks for only .md files
            program_name = handbook_md.name.replace(".md", "")
            document = load_and_clean(handbook_md) #loads the file and cleans it
            split = split_chunk(document, program_name) #splits the file into chunks, first by header then size
            all_chunks.extend(split) #adds all document chunks into a single list to be sent off to chromaDB

        #print(f"Total chunks: {len(all_chunks)}, {split[0].metadata}") #tells us how many chunks have been created and the name of the program
    print(f"Total chunks: {len(all_chunks)}")
    
# opens and cleans the document 
def load_and_clean(filepath):
    with open(filepath, 'r', encoding='utf-8') as file: #we open the file
        document = file.read() #read the file
        document = re.sub(r'\|.*?\.{4,}.*?\|', '', document) #clean the document off '\|.*?\.{4,}.*?\|' and store it back in document
    return document #returns document for main 

    
def split_chunk(markdown, program_name):  #splits the document first by headers, then by size within the headers
    headers_to_split_on = [ #defines the headers to split it by
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3")
]
    # MD splits ---- sets what to split on as defined above and then splits the files passed
    # based on the defined split and stores it in md_header_splits
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on, 
                                               strip_headers=False
                                               )
    md_header_split = markdown_splitter.split_text(markdown)

    # Char-level splits ----- sets the chunk size and how much overlap is within each chunk
    # and splits the header chunks into smaller 700 character chunks to ensure that some chunks are not too big 
    # text_splitter stores the method using the defined sizes and it is applied to the passed document 
    # that has already been split by header to further chunk it by size, which is stored in variable "splits"
    chunk_size = 700
    chunk_overlap = 30
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, 
                                                   chunk_overlap=chunk_overlap
                                                   )
    # Split
    char_split = text_splitter.split_documents(md_header_split)
    for chunk in char_split:
        chunk.metadata["program"] = program_name

    return char_split

main()