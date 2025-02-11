import csv
import datetime
import matplotlib.pyplot as plt
import numpy as np

def read_data(file_path):
    data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            data.append(row)
    return data

def plot_northernmost_observation(data, output_file):
    years = []
    latitudes = []
    for row in data:
        try:
            year = datetime.datetime.strptime(row['Slutdatum'], '%Y-%m-%d').year
            latitude = float(row['Nord'])
            if year not in years:
                years.append(year)
                latitudes.append(latitude)
            else:
                index = years.index(year)
                if latitude > latitudes[index]:
                    latitudes[index] = latitude
        except ValueError:
            continue

    plt.figure()
    plt.plot(years, latitudes, marker='o')
    plt.axhline(y=7585000, color='r', linestyle='--', label='Abisko')
    plt.axhline(y=6164000, color='b', linestyle='--', label='Ystad')
    plt.xlabel('Year')
    plt.ylabel('Latitude (RT 90)')
    plt.title('Northernmost Observation Over Time')
    plt.legend()
    plt.savefig(output_file)
    plt.close()

def plot_observations_per_year(data, output_file):
    years = []
    observations = []
    for row in data:
        try:
            year = datetime.datetime.strptime(row['Slutdatum'], '%Y-%m-%d').year
            if year not in years:
                years.append(year)
                observations.append(1)
            else:
                index = years.index(year)
                observations[index] += 1
        except ValueError:
            continue

    plt.figure()
    plt.plot(years, observations, marker='o')
    plt.xlabel('Year')
    plt.ylabel('Number of Observations')
    plt.title('Observations Per Year')
    plt.savefig(output_file)
    plt.close()

def plot_weekly_observations(data, output_file):
    weeks = [0] * 53
    for row in data:
        try:
            date = datetime.datetime.strptime(row['Slutdatum'], '%Y-%m-%d')
            if date.year == 2022:
                week = date.isocalendar()[1]
                weeks[week] += 1
        except ValueError:
            continue

    total_observations = sum(weeks)
    percentages = [week / total_observations for week in weeks]

    plt.figure()
    plt.bar(range(1, 54), percentages)
    plt.xlabel('Week Number')
    plt.ylabel('Percentage of Observations')
    plt.title('Weekly Observations for 2022')
    plt.savefig(output_file)
    plt.close()

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Analyze butterfly observation data.')
    parser.add_argument('input_file', help='Path to the input CSV file.')
    parser.add_argument('output_prefix', help='Prefix for the output PDF files.')
    args = parser.parse_args()

    data = read_data(args.input_file)
    plot_northernmost_observation(data, f'{args.output_prefix}_northernmost_observation.pdf')
    plot_observations_per_year(data, f'{args.output_prefix}_observations_per_year.pdf')
    plot_weekly_observations(data, f'{args.output_prefix}_weekly_observations.pdf')

if __name__ == '__main__':
    main()
