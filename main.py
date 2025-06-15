import os
from google import genai 
from google.genai import types
from dotenv import load_dotenv
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

command_args = sys.argv


try: 
    user_prompt = command_args[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]
except Exception as e:
    print('failed to retrieve argument, error: ', e)
    sys.exit(1)

try:
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents= messages,
    )
except Exception as e:
    print("request to model failed, error: ", e)
    sys.exit(1)
    
prompt_token = response.usage_metadata.prompt_token_count #type: ignore
response_token = response.usage_metadata.candidates_token_count #type: ignore

if len(command_args) == 3:
    if command_args[2] == "--verbose":
        print(f'User prompt: {user_prompt}')
        print(f'Gemini: {response.text}')
        print(f'Response tokens: {response_token}')
        print(f'Prompt tokens: {prompt_token}')
        

    