import os


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