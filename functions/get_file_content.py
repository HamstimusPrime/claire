import os
import sys

def get_file_content(working_directory, file_path):
    
    abs_path_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_path_working_dir, file_path))
    
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    if not abs_file_path.startswith(abs_path_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    max_characters = 10000
    try:
        with open(abs_file_path, "r") as file:
            num_characters_in_file = len(file.read())
            file.seek(0)
            file_content = file.read(max_characters)
            
            if num_characters_in_file > max_characters:
                return f'{file_content} [...File "{file_path}" truncated at 10000 characters]'
            
            return file_content
        
    except Exception as e:
        print(f'Unable to open file in {abs_file_path},Error:  {str(e)}')
        sys.exit(1)
