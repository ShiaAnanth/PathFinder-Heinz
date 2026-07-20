# PathFinder-Heinz
A retrieval-augmented generation (RAG) system that helps prospective students navigate Carnegie Mellon's Heinz College graduate programs — built from official program handbooks, with source-attributed answers instead of generic chatbot responses. PathFinder@Heinz is a 2.0 Version of PathFinder@CISE, a Retrieval-Augmented Generation (RAG) system designed to help prospective students explore programs in the College of Integrated Science and Engineering (CISE) at James Madison University (JMU). 

## Purpose of this tool
Choosing between Heinz College's programs means digging through dense, overlapping handbooks that don't make comparisons easy. PathFinder@Heinz retrieves the relevant sections across all the program handbooks and generates a direct, cited answer, rather than making a prospective student read multiple documents to find the information they seek.

## Tech Stack
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991?style=flat&logo=openai&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat&logo=langchain&logoColor=white)
![Qdrant](https://img.shields.io/badge/Qdrant-DC244C?style=flat&logo=qdrant&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![RAGAS](https://img.shields.io/badge/RAGAS-Evaluation-orange?style=flat)

## Project Pipeline
```mermaid
graph TD
    A[PDF Handbooks] --> B[pymupdf4llm: cleaned Markdown]
    B --> C[Chunking: MarkdownHeaderTextSplitter + RecursiveCharacterTextSplitter]
    C --> D[text-embedding-3-large: vector embeddings]
    D --> E[Qdrant: persistent vector storage]
    E --> F[similarity_search: top-k chunks]
    F --> G[gpt-4o-mini: source-attributed answer]
```

## Roadmap
Outlined below are the tasks that have been completed in the roadmap as of 7/10/2026. As progress is made, the roadmap checklist will be updated accordingly.
- [x] PDF extraction and cleaning
- [x] Header-aware chunking with metadata
- [x] Embedding and vector storage
- [x] Retrieval + generation with source attribution
- [x] Evaluation dataset (9 questions, source-verified)
- [ ] RAGAS scoring script and results
- [ ] Debugging based on evaluation findings
- [ ] Conversational memory
- [ ] Deployment (Qdrant Cloud + Streamlit, custom interface)

## Author
Built by **Shia Ananth**, M.S. Business Intelligence and Data Analytics student at Heinz College, Carnegie Mellon University, as a summer project to learn and improve knowledge on RAG systems. 
