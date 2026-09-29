
from google import genai
from google.genai import types
client = genai.Client()
user_prompt = input("prompt:")
#system_prompt = "limit your answer to one sentence"
response = client.models.generate_content(
    model = "gemini-flash-lite-latest",
    contents = user_prompt,
    config=types.GenerateContentConfig(
        system_instruction="limit your answer to one sentence. and pretend that you are a pitbull"
    ),

)
print(response.text)
