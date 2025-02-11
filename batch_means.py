import argparse
import matplotlib.pyplot as plt

# Function 1: Read the data
# Some variable names are changed to make the code more readable.
def parse_line(line):
    '''
    Parses and validates a single line of data.
    Returns a tuple (batch, x_val, y_val, v_val) or None if invalid.
    '''
    parts = line.strip().split(',')
    if len(parts) < 4:
        print(f"Warning: wrong input format for entry: {line.strip()}")
        return None
    try:
        batch = parts[0]
        # Convert the values to floats using map
        x_val, y_val, v_val = map(float, parts[1:]) 
        return batch, x_val, y_val, v_val
    except ValueError:
        print(f"Warning: wrong input format for entry: {line.strip()}")
        return None

def read_data(filename):
    '''
    Reads the data from the file and stores it in a dictionary.
    Arguments:
        filename -- the path of the file to read from.
    Returns:
        A dictionary where keys are batch numbers and values are lists of tuples 
        containing the x, y, and value of data points.
    '''
    data = {}
    with open(filename, 'r') as file:
        for line in file:
            parsed = parse_line(line)
            if parsed:
                batch, x_val, y_val, v_val = parsed
                # Use setdefault to create a new list if batch is not in data
                data.setdefault(batch, []).append((x_val, y_val, v_val)) 
                # if batch not in data:
                #     data[batch] = []
                # data[batch].append((x_val, y_val, v_val))   
    return data

# Function 2: Calculate the average for a batch
# Some variable names are changed to make the code more readable.
def calculate_batch_average(sample):
    '''
    Calculates the average value for samples in a batch within the unit circle (x² + y² ≤ 1).
    Arguments:
        sample -- a list of tuples containing the x, y, and value of data points.
    Returns:
        average -- The average value of the data points within the unit circle.
        Returns 0 if none are within the circle.
    '''
    count = 0
    total = 0
    for (x, y, val) in sample:
        if x**2 + y**2 <= 1:
            total += val
            count += 1
    try:
        average = total/count
    except ZeroDivisionError: # If there are no data points within the unit circle
        # This part is move to the print_result function
        # print("No data points within the unit circle")
        average = 0
    return average

# Function 3: Process the data
def process_data(data):
    '''
    Processes all batches to calculate their respective averages
    Arguments:
        data -- a dictionary where keys are batch numbers and values are lists of tuples 
                containing the x, y, and value of data points.
    Returns:
        A dictionary where keys are batch numbers and values are the average value 
        of the data points.
    '''
    result = {}
    for batch, samples in data.items():
        result[batch] = calculate_batch_average(samples)
    return result

# Function 4: Print the result
def print_result(data):
    '''
    Prints the average value for each batch.
    Arguments:
        A dictionary where keys are batch numbers and values are the average value 
        of the data points.
    '''
    print("Batch\t Average")
    for batch in sorted(data.keys(), key=int):  # Sort batch numbers as integers
        avg = data[batch]
        if avg != 0:  # Skip batches with no data points within the unit circle
            print(f"{batch}\t {avg:.1f}")
        else: # error correction: print a message for batches with no data points
            print(f"Batch {batch} has no data points within the unit circle") 

# Function 5: plot the data
def plot_data(data, f, radius):
    '''
    Plots the data points in the dictionary 'data' to a scatter plot and 
    includes the measurement error circle.
    Each data point is labeled with its value.

    Arguments:
        data -- a dictionary where keys are batch numbers and values are lists of tuples 
                containing the x, y, and value of data points.
        f -- the name of the file to save the plot to.
        radius -- the radius of the measurement error circle.
    '''
    fig, ax = plt.subplots()
    for batch, samples in data.items():
        x = [x for x, y, v in samples]
        y = [y for x, y, v in samples]
        values = [v for x, y, v in samples]
        scatter = ax.scatter(x, y, label=f"Batch {batch}")
        for i, txt in enumerate(values):
            ax.annotate(txt, (x[i], y[i]), xytext=(2, 2), textcoords='offset points',
                        color=scatter.get_edgecolor()[0], 
                        fontsize=8)  # Annotate each point with its value in the same color

    # Plot the measurement error circle
    circle = plt.Circle((0, 0), radius, color='b', fill=False)
    ax.add_artist(circle)
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    ax.set_xlim(-radius * 1.1, radius * 1.1)  # Set x-axis limits according to the circle size
    ax.set_ylim(-radius * 1.1, radius * 1.1)  # Set y-axis limits according to the circle size
    fig.set_size_inches(10, 8)
    plt.savefig(f)
    print(f"A plot of the data can be found in {f}")
    # plt.show()

# Main function
def main():
    '''
    This is the main body of the program.
    '''
    parser = argparse.ArgumentParser(description='Process some data.')
    parser.add_argument('radius', type=float, help='the radius of the measurement error') # Add a new argument for the radius
    parser.add_argument('infile', type=str, help='the input file containing the data') # Add a new argument for the input file
    parser.add_argument('outfile', type=str, help='the output file to save the plot') # Add a new argument for the output file
    args = parser.parse_args() # Parse the arguments

    data = read_data(args.infile)
    result = process_data(data)
    print_result(result)
    plot_data(data, args.outfile, args.radius)  # Call plot_data with the specified radius

# Start the main program: this is idiomatic python
if __name__ == '__main__':
    main()
