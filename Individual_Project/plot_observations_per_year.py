import datetime
import matplotlib.pyplot as plt

def process_observations(data):
    """
    Processes the observation data to count the number of observations per year.

    Args:
        data (list): A list of dictionaries containing butterfly observation data.

    Returns:
        dict: A dictionary with years as keys and the number of observations as values.
    """
    year_observations = {}  # dictionary to store the year and the number of observations
    for row in data:
        try:  # try to convert the date to a year and the number of observations to an integer
            year = datetime.datetime.strptime(row['Slutdatum'], '%Y-%m-%d').year
            antal = row['Antal']
            if year not in year_observations:  # if the year is not in the dictionary, add it and the number of observations
                year_observations[year] = antal
            else:  # if the year is in the dictionary, add the number of observations to the existing value
                year_observations[year] += antal
        except ValueError:  # if the data is invalid, it is skipped
            continue

    return dict(sorted(year_observations.items()))  # sort the dictionary by year

def plot_observations_per_year(data):
    """
    Plots the number of observations per year for a butterfly species.

    Args:
        data (list): A list of dictionaries containing butterfly observation data.

    Output:
        A plot of the number of observations per year for a butterfly species.
    """
    sorted_year_observations = process_observations(data)
    artnamn = data[0]['Artnamn']

    plt.figure()
    plt.plot(sorted_year_observations.keys(), sorted_year_observations.values(), marker='o', markersize=3)
    plt.xlabel('Year')
    plt.ylabel('# Observations')
    plt.title(f'{artnamn}: Observations Per Year')
    plt.xticks(range(min(sorted_year_observations.keys()), max(sorted_year_observations.keys())+1, 2))
    plt.savefig(f'{artnamn}_observations_per_year.pdf')
    plt.close()
