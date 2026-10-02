import os
from dotenv import load_dotenv, find_dotenv
from groq import Groq
from langchain_groq import ChatGroq
from langchain_groq import ChatGroq

load_dotenv(find_dotenv())

api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    print("GROQ_API_KEY not found in .env!")
    exit(1)

client = Groq(api_key=api_key)

try:
    models = client.models.list()
    active_models = [m.id for m in models.data if "whisper" not in m.id]
    print("\n--- ACTIVE GROQ CHAT MODELS FOR YOUR KEY ---")
    for model_id in active_models:
        print(f"- {model_id}")
    print("--------------------------------------------\n")

    # Test the first available chat model
    selected_model = active_models[0]
    print(f"Testing inference with: {selected_model} ...")
    chat = client.chat.completions.create(
        model=selected_model,
        messages=[{"role": "user", "content": "Respond with the single word: OK"}],
    )
    print("Response from Groq:", chat.choices[0].message.content)
    print(f"\nSUCCESS! Use this model in your scripts: model_name='{selected_model}'")

except Exception as e:
    print("Error connecting to Groq:", e)
    
    
  