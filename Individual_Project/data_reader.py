import csv

def read_data(file_path):
    """
    Reads butterfly observation data from a CSV file.

    Args:
        file_path (str): Path to the input CSV file.

    Returns:
        list: A list of dictionaries containing butterfly observation data.
    """
    data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            try:
                antal = row['Antal']
                if antal.lower() == 'noterad':
                    antal = 1
                else:
                    antal = int(antal)
                data.append({
                    'Artnamn': row['Artnamn'],
                    'Antal': antal,
                    'Nord': int(row['Nord']),
                    'Slutdatum': row['Slutdatum']
                })
            except (ValueError, KeyError) as e:
                print(f"Warning: Skipping invalid data row: {row}. Error: {e}")
                continue
    return data
