import pandas as pd
import matplotlib.pyplot as plt

DATA_SOURCE = "csv_files"

def select_data():
    """Function that lets you select data from a list"""

    files = ["cities.csv", "example.csv", "homes.csv"]
    print(f"Hey, which dataset would you like to use 1 - {len(files) + 1}")
    index = 1
    for filename in files:
        print(f"{index}. {filename}")
        index += 1
    response = str(input(">"))
    try:
        response = int(response)
        if response > len(files) or response < 1:
            print("Index out of range")
        else:
            print(f"You have selected: {files[response][:-4]}")
            return files[response-1]
    except Exception as e:
        print(e)
    return None

def read_csv(filename):
    """reads filename with DATA_SOURCE"""

    return pd.read_csv(f"{DATA_SOURCE}/{filename}")

def menu_choice():
    """Prints out choices and returns the users response"""

    print("What do you want to do with this data file")
    print("1. Find any duplicate rows")
    print("2. Delete all duplicate rows")
    print("3. View graph")
    response = str(input(">"))
    try:
        response = int(response)
        if response > 3 or response < 1:
            print("Index out of range")
        else:
            return response
    except Exception as e:
        print(e)
    return None

def preview_data(filename):
    """read and print the dataset"""

    df = read_csv(selected_data)
    print(df.to_string())

if __name__ == "__main__":
    selected_data = None
    while selected_data is None:
        selected_data = select_data()
    choice = None
    while choice is None:
        choice = menu_choice()
        
    
        
        