import os
import google.generativeai as genai
from dotenv import load_dotenv
from utils.loader import load_pdf_text, load_csv_text

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Define file paths
pdf_path = "data/prisma-access-administration.pdf"
csv_path = "data/Tasks - Dashboard.csv"

# Load documents if they exist
pdf_text = load_pdf_text(pdf_path) if os.path.exists(pdf_path) else "[PDF not found]"
csv_text = load_csv_text(csv_path) if os.path.exists(csv_path) else "[CSV not found]"
doc_context = pdf_text + "\n\n" + csv_text

# Choose a valid model you confirmed
model = genai.GenerativeModel("models/gemini-1.5-flash")  # you can also try "models/gemini-2.5-pro" later

print("🤖 Gemini Chatbot (stateless mode) with Doc Context (type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    # Combine user prompt with context
    full_prompt = f"{doc_context}\n\nUser question: {user_input}"
    
    response = model.generate_content(full_prompt)
    print(f"Gemini: {response.text}\n")

