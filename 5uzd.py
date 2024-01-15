def write_name_to_file(name, file_path):
    try:
        with open(file_path, 'w') as file:
            file.write(name)
        print(f"Successfully wrote the name '{name}' to the file '{file_path}'.")
    except IOError as e:
        print(f"Error: Unable to write to the file. {e}")
    except Exception as e:
        print(f"Error: Unexpected error. {e}")

if __name__ == "__main__":
    user_name = input("Enter your name: ")

    file_path = 'lietotajs.txt'

    write_name_to_file(user_name, file_path)
