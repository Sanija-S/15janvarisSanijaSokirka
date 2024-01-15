import csv

def read_column_data(csv_file_path, column_index):
    try:
        with open(csv_file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)


            column_data = [row[column_index] for row in reader]

         
            print(f"Data from the {column_index+1} column:")
            for data in column_data:
                print(data)
    except FileNotFoundError:
        print(f"Error: CSV file '{csv_file_path}' not found.")
    except Exception as e:
        print(f"Error: Unable to read the CSV file. {e}")


default_csv_file_path = 'abc.csv'

column_index = 1
read_column_data(default_csv_file_path, column_index)
