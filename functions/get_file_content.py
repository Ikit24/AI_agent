import os

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    absolute_path = os.path.abspath(full_path)
    work_dir_abspath = os.path.abspath(working_directory)

    if not absolute_path.startswith(work_dir_abspath):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    file_content_string = ""
    try:
        with open(full_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            remaining_content = f.read(1)
            if remaining_content != "":
                truncation_msg = f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                file_content_string += truncation_msg
    except Exception as e:
        return f"Error: An error occurred while reading the file: {e}"

    return file_content_string
