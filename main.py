from dotenv import load_dotenv
import os
import requests
import wikipedia
import sys

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"

if not API_KEY:
    print("ERROR: GROQ_API_KEY not found in .env")
    sys.exit(1)

print("API_KEY loaded successfully.")

def fetch_context(topic):
    try:
        return wikipedia.summary(topic, sentences=4)
    except Exception as e:
        print("Warning: could not fetch Wikipedia info:", e)
        return "No background information found."

def generate_with_rag(topic, content_type="blog", tone="informative"):
    context = fetch_context(topic)
    prompt = (
        f"Context information about {topic}:\n{context}\n\n"
        f"Task:\nUsing the above context, generate a {tone} {content_type} post about \"{topic}\". "
        "Make it creative, natural, and well-structured. Include an engaging introduction and a concise conclusion."
    )
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.85
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.HTTPError as e:
        print("HTTP Error:", e)
        print("Response:", response.text)
        sys.exit(1)
    except Exception as e:
        print("Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    print("DeepContent - AI Content Generator\n")
    topic = input("Enter a topic: ").strip()
    content_type = input("Enter content type (blog / caption / post / ad) [blog]: ").strip() or "blog"
    tone = input("Enter tone (informative / engaging / persuasive / casual) [informative]: ").strip() or "informative"
    
    print("\nGenerating AI content...\n")
    output = generate_with_rag(topic, content_type, tone)
    print(output)
