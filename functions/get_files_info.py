import os

def get_files_info(working_directory, directory=None):
    full_path = os.path.join(working_directory, directory)
    absolute_path = os.path.abspath(full_path)
    work_dir_abspath = os.path.abspath(working_directory)
    if not absolute_path.startswith(work_dir_abspath):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
