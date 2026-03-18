# gemini_chat.py

def ask_gemini(question):
    chunks = query_docs(question)
    context = "\n".join([c for chunk in chunks for c in chunk])
    prompt = f"Answer based on the following:\n{context}\n\nQuestion: {question}"
    return gemini_api.generate_text(prompt)

