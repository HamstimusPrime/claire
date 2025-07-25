import os
from google import genai 
from google.genai import types
from dotenv import load_dotenv
import sys
from functions.get_files_info import available_functions
from functions.call_functions import call_function

load_dotenv()
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

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

try:
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents= messages,
        config= types.GenerateContentConfig(system_instruction=system_prompt, tools=[available_functions]),

    )
except Exception as e:
    print("request to model failed, error: ", e)
    sys.exit(1)
    
prompt_token = response.usage_metadata.prompt_token_count #type: ignore
response_token = response.usage_metadata.candidates_token_count #type: ignore
list_of_function_calls = response.function_calls

verbose_flag = "--verbose" in command_args
if list_of_function_calls != None:
    if len(command_args) == 3 and verbose_flag:
        for function_call_part in list_of_function_calls:
            function_call_result = call_function(function_call_part, verbose=verbose_flag)
            try:
                response = function_call_result.parts[0].function_response.response #type: ignore
                if verbose_flag:
                    print(f"-> {function_call_result.parts[0].function_response.response}")#type: ignore
            except Exception as e:
                raise Exception(print(f"fatal error: {e}"))
        # print(f"Calling function: {function_call_part.name}({function_call_part.args})")
else:
    if len(command_args) == 2:
        print(f'User prompt: {user_prompt}')
        print(f'Gemini: {response.text}')
        print(f'Response tokens: {response_token}')
        print(f'Prompt tokens: {prompt_token}')
        

    