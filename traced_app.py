from langchain_openai import ChatOpenAI

# Create the language model
llm = ChatOpenAI(model="gpt-4o-mini")

# Three different prompts
prompts = [
    "Explain what a Python list is in simple terms, with one short example.",

    "Write a three-line welcome message for students starting an AI course.",

    "Explain how a RAG system works, step by step, for a beginner."
]

# Send prompts and print answers
for index, prompt in enumerate(prompts, start=1):
    print(f"\n--- Run {index} ---")
    print(f"Prompt: {prompt}")

    response = llm.invoke(prompt)

    print(f"Answer: {response.content}")