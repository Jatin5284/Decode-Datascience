# file_operations.py

def read_file(file_path):
    """Reads the content of a file and returns it."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Error: The file '{file_path}' does not exist."
    except Exception as e:
        return f"Error: {str(e)}"

def write_to_file(file_path, data):
    """Writes data to a file, overwriting any existing content."""
    try:
        with open(file_path, 'w') as file:
            file.write(data)
        return f"Data written to '{file_path}' successfully."
    except Exception as e:
        return f"Error: {str(e)}"

def append_to_file(file_path, data):
    """Appends data to a file."""
    try:
        with open(file_path, 'a') as file:
            file.write(data)
        return f"Data appended to '{file_path}' successfully."
    except Exception as e:
        return f"Error: {str(e)}"
