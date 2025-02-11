import datetime
import matplotlib.pyplot as plt

def plot_observations_per_year(data):
    """
    Plots the number of observations per year for a butterfly species.

    Args:
        data (list): A list of dictionaries containing butterfly observation data.
    """
    year_observations = {}
    artnamn = data[0]['Artnamn']
    for row in data:
        try:
            year = datetime.datetime.strptime(row['Slutdatum'], '%Y-%m-%d').year
            antal = row['Antal']
            if year not in year_observations:
                year_observations[year] = antal
            else:
                year_observations[year] += antal
        except ValueError:
            continue

    sorted_year_observations = dict(sorted(year_observations.items()))

    plt.figure()
    plt.plot(sorted_year_observations.keys(), sorted_year_observations.values(), marker='o', markersize=3)
    plt.xlabel('Year')
    plt.ylabel('# Observations')
    plt.title(f'{artnamn}: Observations Per Year')
    plt.xticks(range(min(sorted_year_observations.keys()), max(sorted_year_observations.keys())+1, 2))
    plt.savefig(f'{artnamn}_observations_per_year.pdf')
    plt.close()
