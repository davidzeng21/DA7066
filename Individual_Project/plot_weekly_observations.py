import datetime
import matplotlib.pyplot as plt

def plot_weekly_observations(data):
    """
    Plots the weekly observations for a butterfly species in 2022.

    Args:
        data (list): A list of dictionaries containing butterfly observation data.
    """
    weeks = [0] * 53
    artnamn = data[0]['Artnamn']
    for row in data:
        try:
            date = datetime.datetime.strptime(row['Slutdatum'], '%Y-%m-%d')
            if date.year == 2022:
                week = date.isocalendar()[1]
                weeks[week] += row['Antal']
        except ValueError:
            continue

    total_observations = sum(weeks)
    percentages = [week / total_observations for week in weeks]

    # Calculate cumulative percentages
    cumulative = [sum(percentages[:i+1]) for i in range(len(percentages))]

    # Find the weeks for 5% and 95%
    start_week = next(i for i, total in enumerate(cumulative) if total >= 0.05)
    end_week = next(i for i, total in enumerate(cumulative) if total >= 0.95)

    plt.figure()
    plt.bar(range(1, 54), percentages, color=['blue' if start_week <= i <= end_week else 'gray' for i in range(53)])
    plt.xlabel('Week Number')
    plt.ylabel('Percentage of Observations')
    plt.title(f'{artnamn}: Weekly Observations for 2022\nActive from week {start_week} to week {end_week}')
    plt.savefig(f'{artnamn}_weekly_observations.pdf')
    plt.close()
