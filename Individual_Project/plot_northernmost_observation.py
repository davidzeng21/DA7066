import datetime
import matplotlib.pyplot as plt

def plot_northernmost_observation(data):
    """
    Plots the northernmost observation of a butterfly species over time.

    Args:
        data (list): A list of dictionaries containing butterfly observation data.
    """
    year_latitude = {}
    artnamn = data[0]['Artnamn']  # Assuming all rows have the same Artnamn
    for row in data:
        try:
            year = datetime.datetime.strptime(row['Slutdatum'], '%Y-%m-%d').year
            latitude = row['Nord']
            if year not in year_latitude or latitude > year_latitude[year]:
                year_latitude[year] = latitude
        except ValueError:
            continue

    # Sort the dictionary by year
    sorted_year_latitude = dict(sorted(year_latitude.items()))

    plt.figure()
    plt.plot(sorted_year_latitude.keys(), sorted_year_latitude.values(), marker='o', markersize=3)
    plt.axhline(y=7585000, color='tab:red', linestyle='--')
    plt.text(min(sorted_year_latitude.keys()), 7585000, 'Abisko', verticalalignment='bottom')
    plt.axhline(y=6164000, color='tab:red', linestyle='--')
    plt.text(min(sorted_year_latitude.keys()), 6164000, 'Ystad', verticalalignment='bottom')
    plt.xlabel('Year')
    plt.ylabel('Latitude (RT 90)')
    plt.title(f'{artnamn}: Northernmost Observation')
    plt.xticks(range(min(sorted_year_latitude.keys()), max(sorted_year_latitude.keys())+1, 2))
    plt.savefig(f'{artnamn}_northernmost_observation.pdf')
    plt.close()
