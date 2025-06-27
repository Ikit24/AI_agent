import os

def run_python_file(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    absolute_path = os.path.abspath(full_path)
    work_dir_abspath = os.path.abspath(working_directory)

    if not absolute_path.startswith(work_dir_abspath):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(os.path.dirname(full_path)):
        return f'Error: File "{file_path}" not found.'

    if not absolute_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    subprocess.run(run_python.py, capture_output=True, timeout=30)
