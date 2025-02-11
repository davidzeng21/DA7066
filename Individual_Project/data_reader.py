import csv

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
        for row in reader:
            try: # try to convert the number of observations to an integer
                antal = row['Antal']
                if antal.lower() == 'noterad': # if the number of observations is not recorded, it is set to 1
                    antal = 1
                else: # if the number of observations is recorded, it is converted to an integer
                    antal = int(antal)
                data.append({
                    'Artnamn': row['Artnamn'],
                    'Antal': antal,
                    'Nord': int(row['Nord']),
                    'Slutdatum': row['Slutdatum']
                })
            except (ValueError, KeyError) as e: # if the data is invalid, it is skipped
                print("\033[93mWarning\033[0m: Skipping invalid data row:")
                print(f"  Row ID: {reader.line_num}")
                print(f"  Error type: {type(e).__name__}")
                print(f"  Error message: {str(e)}")
                continue
    return data
