import csv
import datetime
import matplotlib.pyplot as plt

def read_data(file_path):
    data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
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
    return data

def plot_northernmost_observation(data):
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

def plot_observations_per_year(data):
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

def plot_weekly_observations(data):
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

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Analyze butterfly observation data.')
    parser.add_argument('input_file', help='Path to the input CSV file.')
    args = parser.parse_args()

    data = read_data(args.input_file)
    plot_northernmost_observation(data)
    plot_observations_per_year(data)
    plot_weekly_observations(data)

if __name__ == '__main__':
    main()
