import argparse
from data_reader import read_data
from plot_northernmost_observation import plot_northernmost_observation
from plot_observations_per_year import plot_observations_per_year
from plot_weekly_observations import plot_weekly_observations

def main():
    parser = argparse.ArgumentParser(description='Analyze butterfly observation data.')
    parser.add_argument('input_file', help='Path to the input CSV file.') 
    args = parser.parse_args() 

    data = read_data(args.input_file) # read the data from the input file
    plot_northernmost_observation(data) # plot the northernmost observation
    plot_observations_per_year(data) # plot the number of observations per year
    plot_weekly_observations(data) # plot the weekly observations

if __name__ == '__main__':
    main()
