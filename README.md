# PathFinder-Heinz
A retrieval-augmented generation (RAG) system that helps prospective students navigate Carnegie Mellon's Heinz College graduate programs — built from official program handbooks, with source-attributed answers instead of generic chatbot responses. PathFinder@Heinz is a 2.0 Version of PathFinder@CISE, a Retrieval-Augmented Generation (RAG) system designed to help prospective students explore programs in the College of Integrated Science and Engineering (CISE) at James Madison University (JMU). 

## Purpose of this tool
Choosing between Heinz College's programs means digging through dense, overlapping handbooks that don't make comparisons easy. PathFinder@Heinz retrieves the relevant sections across all the program handbooks and generates a direct, cited answer, rather than making a prospective student read multiple documents to find the information they seek.

## Project Pipeline
PDF handbooks
   │
   ▼
pymupdf4llm  →  cleaned Markdown
   │
   ▼
MarkdownHeaderTextSplitter + RecursiveCharacterTextSplitter  →  chunks + program metadata
   │
   ▼
text-embedding-3-large  →  vector embeddings
   │
   ▼
Qdrant (Docker)  →  persistent vector storage
   │
   ▼
similarity_search()  →  top-k relevant chunks for a query
   │
   ▼
gpt-4o-mini + constrained prompt  →  source-attributed answer
