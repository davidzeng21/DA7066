# DA7066 Programming techniques for Life Sciences 
### Stockholm University VT25
 
The course covers: 
 * Basic computer science concepts. 
 * Programming in a modern programming language and basic usage of Unix.
 * Data structures and classes.
 * Problem-solving through decomposition into subproblems.
 * Program structure. 

The repository includes the implementations of lecture codes and the solutions of exercises and labs.

## Butterfly Analysis Script

The `butterfly_analysis.py` script reads butterfly observation data from Artportalen CSV files and generates diagrams illustrating the life and distribution of butterflies. The script creates three types of diagrams:
1. Northernmost observation over time
2. Number of observations per year
3. Weekly observations for the year 2022

### Usage

To run the script, use the following command:

```bash
python butterfly_analysis.py <input_file> <output_prefix>
```

- `<input_file>`: Path to the input CSV file containing butterfly observation data.
- `<output_prefix>`: Prefix for the output PDF files.

### Examples

1. Generate diagrams for butterfly observation data:

```bash
python butterfly_analysis.py butterfly_data.csv butterfly_output
```

This will create three PDF files:
- `butterfly_output_northernmost_observation.pdf`
- `butterfly_output_observations_per_year.pdf`
- `butterfly_output_weekly_observations.pdf`
