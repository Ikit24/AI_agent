import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

if len(sys.argv) < 2:
    print("prompt not provided")
    sys.exit(1)

user_prompt = sys.argv[1] 

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

system_prompt = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT"'
model_name = "models/gemini-1.5-pro"

response = client.models.generate_content(
    model=model_name,
    contents=messages,
    config=types.GenerateContentConfig(system_instruction=system_prompt),
)

if "--verbose" in sys.argv:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

print(response.text)
