def main():
    filename = input("Enter the name of the file to read: ")
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    
