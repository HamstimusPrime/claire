import os
from google import genai
from google.genai import types


def get_files_info(working_directory, directory:  str = None): #type: ignore
    if directory == None:
        return f'Error: "{directory}" is not a directory'
    
    #join both paths and validate if its a directory that exists
    abs_path_working_dir = os.path.abspath(working_directory)
    dst_dir = os.path.abspath(os.path.join(working_directory, directory))
    
    #check if joined path is a valid path
    if os.path.isdir(dst_dir) == False:
        return f'Error: "{directory}" is not a directory'
        
    #check if directory is outside the bounds of working directory
    if dst_dir.startswith(abs_path_working_dir) == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    #get list of content in full path directory
    items_in_full_path = os.listdir(dst_dir)
    
    #for each file in list, get file size, and check if file is folder(isdir)
    content_info = ""
    for item in items_in_full_path:
        list_with_file_info = []
        item_full_path = os.path.join(dst_dir, item)
        item_size = f'{os.path.getsize(item_full_path)}'
        item_full_path = os.path.join(dst_dir, item)
        item_is_dir = str(os.path.isdir(item_full_path))
        
        list_with_file_info.append(f'- {item}:')
        list_with_file_info.append(f'file_size={item_size} bytes,')
        list_with_file_info.append(f'is_dir={str(item_is_dir)}')
        list_with_file_info.append("\n")
        content_info += " ".join(list_with_file_info)

    return content_info

schema_get_files_info =  types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the content of a specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative file-path to the file to be read.",
            ),
        },
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute Python files with optional arguments.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative file-path to the python program to be executed.",
            ),
        },
    ),
)


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write text to file in the file-path provided.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative file-path of the file to be written.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The string/text to be written.",
            ),
        },
    ),
)



available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info, schema_get_file_content, schema_run_python_file, schema_write_file,
    ]
)