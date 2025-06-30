import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai
from google.genai import types
#from google.generativeai.types import FunctionDeclaration, Schema, Type
from functions.get_files_info import schema_get_files_info

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

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)

model_name = "models/gemini-1.5-flash"

config = types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=system_prompt
)

response = client.models.generate_content(
    model=model_name,
    contents=messages,
    config=config
)

if "--verbose" in sys.argv:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if response.function_calls:
    for i in response.function_calls:
        print(f"Calling function: {i.name}({i.args})")
else:
    print(f"{response.text}")
