def write_file(file_name, file_content):
     
     with open(f"{file_name}.txt", "w", encoding="utf-8") as file:
        file.write(file_content)


def append_file(file_name, append_content):

    with open(f"{file_name}.txt", "a", encoding="utf-8") as file:
        file.write(append_content)

def read_file(file_name):
    try:
        with open(f"{file_name}.txt", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None
