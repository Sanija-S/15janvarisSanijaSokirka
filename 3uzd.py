import csv

def read_third_column(csv_file_path):
    try:
        with open(csv_file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)

            # Read only the third column data
            third_column_data = [row[2] for row in reader]

            # Print the third column data
            print("Data from the third column:")
            for data in third_column_data:
                print(data)
    except FileNotFoundError:
        print(f"Error: CSV file '{csv_file_path}' not found.")
    except Exception as e:
        print(f"Error: Unable to read the CSV file. {e}")

# User input - Enter the path to your CSV file
csv_file_path = input("Enter the CSV file path (e.g., abc.csv): ")

# Call the function, passing the user-entered CSV file path
read_third_column(csv_file_path)
