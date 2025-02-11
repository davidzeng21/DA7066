import datetime
import matplotlib.pyplot as plt

def plot_northernmost_observation(data):
    """
    Plots the northernmost observation of a butterfly species over time.

    Args:
        data (list): A list of dictionaries containing butterfly observation data.

    Output:
        A plot of the northernmost observation of a butterfly species over time.
    """
    year_latitude = {} # dictionary to store the year and the latitude of the northernmost observation
    artnamn = data[0]['Artnamn']  # Assuming all rows have the same Artnamn
    for row in data:
        try: # try to convert the date to a year and the latitude to an integer
            year = datetime.datetime.strptime(row['Slutdatum'], '%Y-%m-%d').year
            latitude = row['Nord']
            # if the year is not in the dictionary, or the latitude is greater than the latitude in the dictionary, 
            # add the year and latitude to the dictionary
            if year not in year_latitude or latitude > year_latitude[year]: 
                year_latitude[year] = latitude 
        except ValueError: # if the data is invalid, it is skipped
            continue

    sorted_year_latitude = dict(sorted(year_latitude.items())) # sort the dictionary by year

    plt.figure()
    plt.plot(sorted_year_latitude.keys(), sorted_year_latitude.values(), marker='o', markersize=3)
    plt.axhline(y=7585000, color='tab:red', linestyle='--')
    plt.text(min(sorted_year_latitude.keys()), 7585000, 'Abisko', verticalalignment='bottom') # add the line label to the plot
    plt.axhline(y=6164000, color='tab:red', linestyle='--')
    plt.text(min(sorted_year_latitude.keys()), 6164000, 'Ystad', verticalalignment='bottom')
    plt.xlabel('Year')
    plt.ylabel('Latitude (RT 90)')
    plt.title(f'{artnamn}: Northernmost Observation')
    plt.xticks(range(min(sorted_year_latitude.keys()), max(sorted_year_latitude.keys())+1, 2)) # set the x-axis to show every second year
    plt.savefig(f'{artnamn}_northernmost_observation.pdf')
    plt.close()
