from dotenv import load_dotenv
import os
import asyncio  #Python's built-in library for running async code, code is sometimes kept in waiting when other parts process, asyncio helps regulate that
from openai import AsyncOpenAI # AsyncOpenAI is OpenAI's own official Python library without relying on langchain
from ragas.llms import llm_factory
from ragas.metrics.collections import Faithfulness, ContextPrecision
from generate import retrieve, generate_answer, detect_program
from evaluate import eval_data


# Setup LLM
load_dotenv()

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY")) 
eval_llm = llm_factory("gpt-4o-mini", client=client)
#connects to the grader llm
faithfulness_scorer = Faithfulness(llm=eval_llm) 
precision_scorer = ContextPrecision(llm=eval_llm)


async def run_all_faithfulness_checks(): #checks how factually consistent a response is with the retrieved context
    results = [] #create an empty list
    for item in eval_data: #for every item from our evaluation grader list
        question = item["question"] #choose key "question"
        detected_programs = detect_program(question) #runs detect program on that question 
        chunks = retrieve(question, programs=detected_programs) #uses question and program name to retrieve chunks
        retrieved_texts = [chunk.page_content for chunk in chunks] # organizes retrived chunks
        answer = generate_answer(question) #generates a response using the LLM 

        result = await faithfulness_scorer.ascore( #takes the question, response and the chunks to score for faithfulness
            user_input=question,
            response=answer,
            retrieved_contexts=retrieved_texts,
        )
        #adds the question, response and the faithfulness score to the results list 
        results.append({ 
            "question": question,
            "answer": answer,
            "faithfulness": result.value,
        })

        print(f"Q: {question}")
        print(f"Faithfulness: {result.value}\n")

    return results #outputs the results list


async def run_context_precision_checks(): #checks how relevant the retrived chunks are
    results = []
    for item in eval_data:
        question = item["question"]
        reference = item["expected_answer"]


        detected_programs = detect_program(question)
        chunks = retrieve(question, programs=detected_programs)
        retrieved_texts = [chunk.page_content for chunk in chunks]

        result = await precision_scorer.ascore(
            user_input=question,
            reference=reference,
            retrieved_contexts=retrieved_texts,
        )

        results.append({
            "question": question,
            "context_precision": result.value,
        })

        print(f"Q: {question}")
        print(f"Context Precision: {result.value}\n")

    return results
       

if __name__ == "__main__":
    print("=== FAITHFULNESS ===")
    faithfulness_results = asyncio.run(run_all_faithfulness_checks())

    print("\n=== CONTEXT PRECISION ===")
    precision_results = asyncio.run(run_context_precision_checks())

    print("\n--- SUMMARY ---")
    for f, p in zip(faithfulness_results, precision_results):
        print(f"Faithfulness: {f['faithfulness']:.2f} | Context Precision: {p['context_precision']:.2f} — {f['question']}")