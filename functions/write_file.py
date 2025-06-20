import os

def write_file(working_directory, file_path, content = None):
    
    if not content:
        return f'Error: No fiile content provided to write, content: {content}'
    
    abs_path_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_path_working_dir,file_path))
    file_dir = os.path.dirname(abs_file_path)
    

    if not file_dir.startswith(abs_path_working_dir):
        print("...Aborting: file path outside working directory")
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    print(f'...creating directory at: {file_dir}')
    os.makedirs(file_dir, exist_ok= True)

    try:
        with open(abs_file_path, 'w') as file:
            file.write(content)
        
    except Exception as e:
        print(f'Error: Unable to write content to file at: {abs_file_path}, error: {str(e)}')
        
    return f'Successfully wrote to "{abs_file_path}" ({len(content)} characters written)'