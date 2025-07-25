from google import genai
from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python import run_python_file
from functions.write_file import write_file



def call_function(function_call_part: types.FunctionCall, verbose=False):
    if not verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    
    function_call_part.args["working_directory"] = "./calculator"#type: ignore
    
    function_names = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }
    
    if function_call_part.name not in function_names:
        return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,#type: ignore
                response={"error": f"Unknown function: {function_call_part.name}"},
            )
            ],
        )
        
    function_result = function_names[function_call_part.name](**function_call_part.args)#type: ignore
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,#type: ignore
                response={"result": function_result},
            )
        ],
    )

    