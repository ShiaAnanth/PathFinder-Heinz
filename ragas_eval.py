from dotenv import load_dotenv
import os
import asyncio  #Python's built-in library for running async code, code is sometimes kept in waiting when other parts process, asyncio helps regulate that
from openai import AsyncOpenAI # AsyncOpenAI is OpenAI's own official Python library without relying on langchain
from ragas.llms import llm_factory
from ragas.metrics.collections import Faithfulness
from generate import retrieve, generate_answer

# Setup LLM
load_dotenv()

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY")) 
eval_llm = llm_factory("gpt-4o-mini", client=client)
scorer = Faithfulness(llm=eval_llm)  #connects to the grader llm


'''
async def run_faithfulness_check(question):
    chunks = retrieve(question) #returns the top 5 similar results based on the question
    retrieved_texts = [chunk.page_content for chunk in chunks] # for each chunk in the retrieved chunks, it retrives the text content from it
    answer = generate_answer(question) #returns the answer to the question

    print("QUESTION:", question)
    print("\nANSWER:", answer)
    print("\nRETRIEVED CONTEXTS:")
    for i, text in enumerate(retrieved_texts, 1):
        print(f"[{i}] {text[:200]}")


    result = await scorer.ascore(
    user_input=question,
    response=answer,
    retrieved_contexts=retrieved_texts,

)
    return result.value

if __name__ == "__main__":
    question = "What extra core classes do I need for MISM BIDA compared to MISM?"
    score = asyncio.run(run_faithfulness_check(question))
    print(f"Faithfulness score: {score}")
'''

questions = [
    "What is the difference between the msppm and the msppm-da programs?",
    "Does AIM have an internship requirement?",
    "What extra core classes do I need for MISM BIDA compared to MISM?",
    "I am interested in managing and designing video games, which program should I choose?",
    "How is MSIT different from MISM?",
    "Can I take a gap year?",
    "How do I take classes outside of Heinz college?",
    "I want to break into the health care industry, what should I pursue?",
    "What is the weather like in pittsburgh?",
    "How long can I wait to add/drop classes at Heinz?",
]


async def run_all_faithfulness_checks():
    results = []
    for question in questions:
        chunks = retrieve(question)
        retrieved_texts = [chunk.page_content for chunk in chunks]
        answer = generate_answer(question)

        result = await scorer.ascore(
            user_input=question,
            response=answer,
            retrieved_contexts=retrieved_texts,
        )

        results.append({
            "question": question,
            "answer": answer,
            "faithfulness": result.value,
        })

        print(f"Q: {question}")
        print(f"Faithfulness: {result.value}\n")

    return results

if __name__ == "__main__":
    results = asyncio.run(run_all_faithfulness_checks())
    print("\n--- SUMMARY ---")
    for r in results:
        print(f"{r['faithfulness']:.2f} — {r['question']}")