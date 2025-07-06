import os, subprocess


def run_python_file(working_directory, file_path):
    abs_path_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_path_working_dir, file_path))
    
    if not abs_file_path.startswith(abs_path_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    #run file using the subprocess module:
    try:
        output = subprocess.run(["python", abs_file_path], timeout=30, capture_output=True, cwd= abs_path_working_dir, text=True)
        return_code = output.returncode 
        if output.stdout == "" and output.stderr == "": 
            return "No output produced."

        output_string = ""
        if output.stdout != "":
            output_string += f"STDOUT:{output.stdout} "
        
        if output.stderr != "":
            output_string += f"STDERR:{output.stderr} "
        
        if return_code != 0:
            output_string += f"Process exited with code {return_code} "
            
        return output_string

    except Exception as e:
        return f"Error: executing Python file: {e}"


