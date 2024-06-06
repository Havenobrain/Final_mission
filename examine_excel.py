import pandas as pd

def examine_excel(file_path, sheet_name):
    # Read the Excel file, skipping the first row and using the second row as headers
    data = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl', header=1)
    
    # Print the first few rows of the data
    print("First few rows of the Excel sheet with headers:")
    print(data.head())

if __name__ == "__main__":
    file_path = '/Users/georgijsergeev/Desktop/GODBLESSME/silant_service/data/МЃ© С®Ђ†≠в §†≠≠л• §Ђп нЂ•™ваЃ≠≠Ѓ£Ѓ ѓ†бѓЃав† output.xlsx'
    sheet_name = 'рекламация output'  # название листа
    examine_excel(file_path, sheet_name)


