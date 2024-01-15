import csv

def read_second_column(csv_file_path):
    try:
        with open(csv_file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)

            # Read only the second column data
            second_column_data = [row[1] for row in reader]

            # Print the second column data
            print("Data from the second column:")
            for data in second_column_data:
                print(data)
    except FileNotFoundError:
        print(f"Error: CSV file '{csv_file_path}' not found.")
    except Exception as e:
        print(f"Error: Unable to read the CSV file. {e}")

csv_file_path = input("Enter the CSV file path: ")


read_second_column(csv_file_path)
