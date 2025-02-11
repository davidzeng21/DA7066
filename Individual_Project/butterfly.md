# Butterfly Analysis

The `butterfly_analysis.py` script reads butterfly observation data from Artportalen CSV files and generates diagrams illustrating the life and distribution of butterflies. The script creates three types of diagrams:
1. Northernmost observation over time
2. Number of observations per year
3. Weekly observations for the year 2022

## Usage

To run the script, use the following command:

```bash
python main.py <input_file>
```

- `<input_file>`: Path to the input CSV file containing butterfly observation data.

## Examples

1. Generate diagrams for butterfly observation data:

```bash
python main.py butterfly_data.csv
```

This will create three PDF files:
- `butterfly_data_northernmost_observation.pdf`
- `butterfly_data_observations_per_year.pdf`
- `butterfly_data_weekly_observations.pdf`

## Program and Tasks Implemented

The program implemented is a butterfly analysis script that reads butterfly observation data from a CSV file and generates diagrams illustrating the life and distribution of butterflies. The tasks implemented include:
1. Reading butterfly observation data from a CSV file.
2. Generating diagrams for northernmost observation over time, number of observations per year, and weekly observations for the year 2022.

## Libraries/Modules Used

The following libraries/modules are used in the program:
1. `csv`: To read the input CSV file.
2. `datetime`: To handle date and time operations.
3. `matplotlib.pyplot`: To generate and save the diagrams.

These libraries/modules are part of Python's standard distribution and do not require additional installation.

## Program Structure

The program is structured into the following files:
1. `data_reader.py`: Contains the `read_data` function to read butterfly observation data from a CSV file.
2. `plot_northernmost_observation.py`: Contains the `plot_northernmost_observation` function to generate the northernmost observation diagram.
3. `plot_observations_per_year.py`: Contains the `plot_observations_per_year` function to generate the number of observations per year diagram.
4. `plot_weekly_observations.py`: Contains the `plot_weekly_observations` function to generate the weekly observations for the year 2022 diagram.
5. `main.py`: Contains the main script logic and argument parsing.

## Algorithms Used

The program uses the following algorithms:
1. Reading and parsing CSV data.
2. Extracting and processing date and latitude information.
3. Generating diagrams using matplotlib.

## Data Structures Used

The program uses the following data structures:
1. Lists: To store butterfly observation data.
2. Dictionaries: To store processed data for generating diagrams.

## Answers to the Questions

### Which species appear to have moved northward?
The species that appear to have moved northward can be identified by analyzing the northernmost observation over time. By examining the generated diagram for the northernmost observation, we can observe which species have shown a trend of moving northward over the years.

### Is the number of observations roughly constant over the years?
The number of observations over the years can be analyzed using the diagram for the number of observations per year. By examining this diagram, we can determine if the number of observations has remained roughly constant or if there have been significant changes over time.

### Are there any patterns in the times when butterflies are active? Are there differences between species?
The weekly observations for the year 2022 can be analyzed to identify patterns in the times when butterflies are active. By examining the bar chart showing the percentage of observations per week, we can observe any patterns in butterfly activity. Additionally, by comparing the weekly observations for different species, we can identify any differences in their activity patterns.
