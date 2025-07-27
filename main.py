import os
from google import genai 
from google.genai import types
from dotenv import load_dotenv
import sys
from functions.call_functions import call_function
from functions.get_files_info import available_functions


load_dotenv()
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files
All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
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
    
for i in range(20):
    try:
        response = client.models.generate_content(
            model='gemini-2.0-flash-001', 
            contents= messages,
            config= types.GenerateContentConfig(system_instruction=system_prompt, tools=[available_functions]),
        )
    except Exception as e:
        print("request to model failed, error: ", e)
        sys.exit(1)
        
    if not response.function_calls:
        print("Final response:", response.text)
        break
    
    for candidate in response.candidates:#type: ignore
        messages.append(candidate.content)#type: ignore
    
    list_of_function_calls = response.function_calls
    verbose_flag = "--verbose" in command_args
    
    if list_of_function_calls != None:
        for function_call_part in list_of_function_calls:
            try:
                function_call_result = call_function(function_call_part, verbose=verbose_flag)
            except Exception as e:
                raise Exception(f"fatal error: {e}")
            
            messages.append(function_call_result)

    