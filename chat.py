
from google import genai

client = genai.Client()
response = client.models.generate_content(
    model = "gemini-flash-lite-latest",
    contents = "how to get CS50 certificate free?",

)
print(response.text)
