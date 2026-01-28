import pandas as pd

def display_first_10_rows(file_name):
    try:
        # Load the CSV file
        data = pd.read_csv(file_name)
        
        # Retrieve the first 10 rows
        first_10_rows = data.head(10)
        
        # Display the first 10 rows
        print(first_10_rows.to_string(index=False))
        
    except FileNotFoundError:
        print("The file does not exist")
    except pd.errors.EmptyDataError:
        print("The file is empty")
    except pd.errors.ParserError:
        print("Error parsing the file")

def add_column_and_save(file_name):
    try:
        # Load the CSV file
        data = pd.read_csv(file_name)
        
        # Add a new column
        data = data.assign(status="active")
        
        # Save to a new CSV file
        new_file_name = "modified_data.csv"
        data.to_csv(new_file_name, index=False)
        
        print(f"Modified data saved to {new_file_name}")
        
    except FileNotFoundError:
        print("The file does not exist")
    except pd.errors.EmptyDataError:
        print("The file is empty")
    except pd.errors.ParserError:
        print("Error parsing the file")

def drop_column_and_save(file_name):
    try:
        # Load the CSV file
        data = pd.read_csv(file_name)
        
        # Drop a column
        data = data.drop(columns=["status"], errors="ignore")
        
        # Save to a new CSV file
        new_file_name = "modified_data.csv"
        data.to_csv(new_file_name, index=False)
        
        print(f"Modified data saved to {new_file_name}")
        
    except FileNotFoundError:
        print("The file does not exist")
    except pd.errors.EmptyDataError:
        print("The file is empty")
    except pd.errors.ParserError:
        print("Error parsing the file")

def main():
    display_first_10_rows("data.csv")
    add_column_and_save("data.csv")
    drop_column_and_save("modified_data.csv")

if __name__ == "__main__":
    main()