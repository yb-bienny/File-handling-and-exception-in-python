def modify_content(content):
    """
    Modify the file content.
    Convert all text to uppercase.
    """
    return content.upper()

def main():
    input_filename = "input.txt"       
    output_filename = "modified.txt"   
    try:
        with open(input_filename, "r") as file:
            original_content = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
        return  

    modified_content = modify_content(original_content)
    
    try:
        with open(output_filename, "w") as file:
            file.write(modified_content)
        print(f"Modified content successfully written to '{output_filename}'.")
    except IOError:
        print(f"Error: Could not write to the file '{output_filename}'.")



