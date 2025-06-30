import os
import google.generativeai.types as types

def get_files_info(working_directory, directory=None):
    full_path = os.path.join(working_directory, directory)
    absolute_path = os.path.abspath(full_path)
    work_dir_abspath = os.path.abspath(working_directory)

    if not absolute_path.startswith(work_dir_abspath):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'

    try:
        dir_list = os.listdir(full_path)
        lines = []
        for item in  dir_list:
            item_full_path = os.path.join(full_path, item)
            is_dir = os.path.isdir(item_full_path)
            dir_size = os.path.getsize(item_full_path)
            formatted_line = f"- {item}: file_size={dir_size} bytes, is_dir={is_dir}"
            lines.append(formatted_line)
        return "\n".join(lines)

    except Exception as e:
        return f"Error: {str(e)}"

schema_get_files_info =types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory":types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)


