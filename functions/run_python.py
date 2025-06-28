import os, subprocess

def run_python_file(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    absolute_path = os.path.abspath(full_path)
    work_dir_abspath = os.path.abspath(working_directory)

    if not absolute_path.startswith(work_dir_abspath):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'

    if not absolute_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        filename = os.path.basename(file_path)
        result = subprocess.run(['python3', filename],
                                capture_output=True,
                                timeout=30,
                                cwd=working_directory)

        stdout_str = result.stdout.decode('utf-8')
        stderr_str = result.stderr.decode('utf-8')

        output = ""
        if stdout_str:
            output += f"STDOUT:{stdout_str}"
        if stderr_str:
            output += f"STDERR:{stderr_str}"

        if result.returncode != 0:
            output += f"Process exited with code {result.returncode}"

        if not output:
            return "No output produced."

        return output

    except Exception as e:
            return f"Error: executing Python file: {e}"
