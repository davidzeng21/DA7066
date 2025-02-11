import datetime
import matplotlib.pyplot as plt

def plot_weekly_observations(data):
    """
    Plots the weekly observations for a butterfly species in 2022.

    Args:
        data (list): A list of dictionaries containing butterfly observation data.

    Output:
        A plot of the weekly observations for a butterfly species in 2022.
    """
    weeks = [0] * 53
    artnamn = data[0]['Artnamn']
    for row in data:
        try: 
            date = datetime.datetime.strptime(row['Slutdatum'], '%Y-%m-%d')
            if date.year == 2022: 
                week = date.isocalendar()[1] # get the week number 
                weeks[week] += row['Antal'] # add the number of observations to the week number
        except ValueError: # if the data is invalid, it is skipped
            continue

    total_observations = sum(weeks) # calculate the total number of observations
    percentages = [week / total_observations for week in weeks] # calculate the percentage of observations for each week

    cumulative = [sum(percentages[:i+1]) for i in range(len(percentages))] # calculate the cumulative percentage of observations

    start_week = next(i for i, total in enumerate(cumulative) if total >= 0.05) # find the week for 5%
    end_week = next(i for i, total in enumerate(cumulative) if total >= 0.95) # find the week for 95%

    plt.figure()
    plt.bar(range(1, 54), percentages, color=['blue' if start_week <= i <= end_week else 'gray' for i in range(53)]) # plot the bars and highlight the active weeks
    plt.xlabel('Week Number')
    plt.ylabel('Percentage of Observations')
    plt.title(f'{artnamn}: Weekly Observations for 2022\nActive from week {start_week} to week {end_week}') # add active weeks to the title
    plt.savefig(f'{artnamn}_weekly_observations.pdf')
    plt.close()
