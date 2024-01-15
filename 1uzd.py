def read_and_print(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: Unable to read the file. {e}")

if __name__ == "__main__":
    file_path = "hello.txt"  
    read_and_print(file_path)
