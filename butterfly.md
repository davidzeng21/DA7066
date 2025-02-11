# Butterfly Analysis Script

The `butterfly_analysis.py` script reads butterfly observation data from Artportalen CSV files and generates diagrams illustrating the life and distribution of butterflies. The script creates three types of diagrams:
1. Northernmost observation over time
2. Number of observations per year
3. Weekly observations for the year 2022

## Usage

To run the script, use the following command:

```bash
python butterfly_analysis.py <input_file> <output_prefix>
```

- `<input_file>`: Path to the input CSV file containing butterfly observation data.
- `<output_prefix>`: Prefix for the output PDF files.

## Examples

1. Generate diagrams for butterfly observation data:

```bash
python butterfly_analysis.py butterfly_data.csv butterfly_output
```

This will create three PDF files:
- `butterfly_output_northernmost_observation.pdf`
- `butterfly_output_observations_per_year.pdf`
- `butterfly_output_weekly_observations.pdf`

## Answers to the questions

### Which species appear to have moved northward?
The species that appear to have moved northward can be identified by analyzing the northernmost observation over time. By examining the generated diagram for the northernmost observation, we can observe which species have shown a trend of moving northward over the years.

### Is the number of observations roughly constant over the years?
The number of observations over the years can be analyzed using the diagram for the number of observations per year. By examining this diagram, we can determine if the number of observations has remained roughly constant or if there have been significant changes over time.

### Are there any patterns in the times when butterflies are active? Are there differences between species?
The weekly observations for the year 2022 can be analyzed to identify patterns in the times when butterflies are active. By examining the bar chart showing the percentage of observations per week, we can observe any patterns in butterfly activity. Additionally, by comparing the weekly observations for different species, we can identify any differences in their activity patterns.
