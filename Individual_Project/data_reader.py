import csv
def process_row(row, line_num):
    """
    Processes a single row of butterfly observation data.

    Args:
        row (dict): A dictionary representing a row of data.
        line_num (int): The line number of the row in the CSV file.

    Returns:
        dict or None: A dictionary with processed data or None if the row is invalid.
    """
    try: # try to convert the number of observations to an integer
        antal = row['Antal']
        if antal.lower() == 'noterad': # if the number of observations is not recorded, it is set to 1
            antal = 1
        else:
            antal = int(antal)
        return {
            'Artnamn': row['Artnamn'],
            'Antal': antal,
            'Nord': int(row['Nord']),
            'Slutdatum': row['Slutdatum']
        }
    except (ValueError, KeyError) as e: # if the data is invalid, it is skipped
        print("\033[93mWarning\033[0m: Skipping invalid data row:")
        print(f"  Row ID: {line_num}")
        print(f"  Error type: {type(e).__name__}")
        print(f"  Error message: {str(e)}")
        return None

def read_data(file_path):
    """
    Reads butterfly observation data from a CSV file.

    Args:
        file_path (str): Path to the input CSV file.

    Returns:
        list: A list of dictionaries containing a subset of the butterfly observation data.
    """
    data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader: # process each row in the CSV file
            processed_row = process_row(row, reader.line_num)
            if processed_row: # if the row is valid, it is added to the list
                data.append(processed_row)
    return data


