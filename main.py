import os
from google import genai
from dotenv import load_dotenv
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

command_args = sys.argv
try: 
    arg = command_args[1]
except Exception as e:
    print('failed to retrieve argument, error: ', e)
    sys.exit(1)

try:
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents= arg 
    )
except Exception as e:
    print("request to model failed, error: ", e)
    sys.exit(1)
    
prompt_token = response.usage_metadata.prompt_token_count
response_token = response.usage_metadata.candidates_token_count


print(f'Gemini: {response.text}')
print(f'Prompt tokens: {prompt_token}\nResponse tokens: {response_token}')   