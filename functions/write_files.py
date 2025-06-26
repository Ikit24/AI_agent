import os

def write_file(working_directory, file_path, content):
    full_path = os.path.join(working_directory, file_path)
    absolute_path = os.path.abspath(full_path)
    work_dir_abspath = os.path.abspath(working_directory)

    if not absolute_path.startswith(work_dir_abspath):
            return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'

    try:
        if not os.path.exists(os.path.dirname(full_path)):
            os.makedirs(os.path.dirname(full_path), mode=0o777)
    except Exception as e:
        return f"Error: An error occured while creating directory: {e}" 

    with open(full_path, "w") as f:
        f.write(content)

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

