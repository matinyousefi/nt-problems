import os
from openai import OpenAI

# Make sure you have:
# pip install openai
# and set your environment variable: export OPENAI_API_KEY="your_api_key"

client = OpenAI()

def translate_text(text, source_lang="English", target_lang="French"):
    prompt = f"Translate the following {source_lang} text to {target_lang}:\n\n{text}"

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or gpt-4o, gpt-4.1, etc.
        messages=[
            {"role": "system", "content": "You are a professional translator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    source_text = input("Enter the text to translate: ")
    src_lang = input("Source language (default: English): ") or "English"
    tgt_lang = input("Target language (default: French): ") or "French"

    translation = translate_text(source_text, src_lang, tgt_lang)
    print(f"\n--- Translation ({src_lang} → {tgt_lang}) ---\n{translation}")
