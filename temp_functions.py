def fahrenheit_to_celsius(t):
    """
    Convert Fahrenheit to Celsius.
    """
    t_celsius = (t - 32) * 5/9
    return round(t_celsius, 2)

def celsius_to_fahrenheit(t):
    """
    Convert Celsius to Fahrenheit.
    """
    t_fahrenheit = t * 9/5 + 32
    return round(t_fahrenheit, 2)

def kelvin_to_celsius(t):
    """
    Convert Kelvin to Celsius.
    """
    t_celsius = t - 273.15
    return round(t_celsius, 2)

def celsius_to_kelvin(t):
    """
    Convert Celsius to Kelvin.
    """
    t_kelvin = t + 273.15
    return round(t_kelvin, 2)

def kelvin_to_fahrenheit(t):
    """
    Convert Kelvin to Fahrenheit.
    """
    t_fahrenheit = (t - 273.15) * 9/5 + 32
    return round(t_fahrenheit, 2)

def fahrenheit_to_kelvin(t):
    """
    Convert Fahrenheit to Kelvin.
    """
    t_kelvin = (t - 32) * 5/9 + 273.15
    return round(t_kelvin, 2)

# # Main loop for user input/output interaction
# input_temps = []
# output_temps = []
# 
# loop = True
# while loop:
#     # Prompt user to select temperature type or quit
#     input_type = input("Choose input type, 'K' for Kelvin, 'F' for Fahrenheit, 'C' for Celsius or 'q' for quit: ")
#     if input_type == 'q':
#         # Print lists and exit
#         loop = False
#         print("Input temperatures: ", input_temps)
#         print("Output temperatures: ", output_temps)
#         print("Goodbye!")
#     elif input_type == 'K':
#         # User chose Kelvin as input
#         temp = float(input("Enter the temperature in Kelvin: "))
#         output_type = input("Choose output type, 'F' for Fahrenheit, 'C' for Celsius: ")
#         if output_type == 'F':
#             # Convert Kelvin to Fahrenheit
#             output_temp = kelvin_to_fahrenheit(temp)
#         elif output_type == 'C':
#             # Convert Kelvin to Celsius
#             output_temp = kelvin_to_celsius(temp)
#         else:
#             print("Invalid choice.")
#         print("The temperature is ", output_temp, output_type)
#         input_temps.append(temp)
#         output_temps.append(output_temp)
#     elif input_type == 'F':
#         # User chose Fahrenheit as input
#         temp = float(input("Enter the temperature in Fahrenheit: "))
#         output_type = input("Choose output type, 'C' for Celsius, 'K' for Kelvin: ")
#         if output_type == 'C':
#             # Convert Fahrenheit to Celsius
#             output_temp = fahrenheit_to_celsius(temp)
#         elif output_type == 'K':
#             # Convert Fahrenheit to Kelvin
#             output_temp = fahrenheit_to_kelvin(temp)
#         else:
#             print("Invalid choice.")
#         print("The temperature is ", output_temp, output_type)
#         input_temps.append(temp)
#         output_temps.append(output_temp)
#     elif input_type == 'C':
#         # User chose Celsius as input
#         temp = float(input("Enter the temperature in Celsius: "))
#         output_type = input("Choose output type, 'F' for Fahrenheit, 'K' for Kelvin: ")
#         if output_type == 'F':
#             # Convert Celsius to Fahrenheit
#             output_temp = celsius_to_fahrenheit(temp)
#         elif output_type == 'K':
#             # Convert Celsius to Kelvin
#             output_temp = celsius_to_kelvin(temp)
#         else:
#             print("Invalid choice.")
#         print("The temperature is ", output_temp, output_type)
#         input_temps.append(temp)
#         output_temps.append(output_temp)
#     else:
#         # Handle invalid input
#         print("Invalid choice.")
# 