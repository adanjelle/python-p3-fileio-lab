
def write_file(file_name, file_content):
    # Ensure the file name has a .txt extension
    file_name = f"{file_name}.txt"
    # Open the file in write mode, which will overwrite any existing content
    with open(file_name, 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    # Ensure the file name has a .txt extension
    file_name = f"{file_name}.txt"
    # Open the file in append mode, which will add content to the end of the file
    with open(file_name, 'a') as file:
        file.write(append_content)

def read_file(file_name):
    # Ensure the file name has a .txt extension
    file_name = f"{file_name}.txt"
    # Open the file in read mode and return its content
    with open(file_name, 'r') as file:
        return file.read()
