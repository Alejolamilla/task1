
# Define a function for validate if the input is valid
def calculator_validator(calculator):
    allowed_values = [0,1]

    if calculator in allowed_values:
        return True
    
    else: 
        return False

#----------------------------------------------------------------------------

#Calculator Selection
print("What do you want to calculate?")
calculator = int(input("Type 0 for density or 1 for velocity."))

#----------------------------------------------------------------------------

if calculator_validator(calculator) == True:

    if calculator == 0:
            
        # Define the variables
        mass = float(input("Enter the mass in kg: "))
        volume = float(input("Enter the volume in m^3: "))

        # Dont allow 0 as input for the divisor since we cant divide by 0
        while volume == 0:
            print("volume can't be 0")
            volume = float(input("Enter the volume in m^3: "))

        # Calculate the density
        density = mass / volume

        # Print the result
        print("Density: " + str(density) + " kg/m^3")

    elif calculator == 1:
        # Define the variables
        time = float(input("Enter the time in seconds: "))
        distance = float(input("Enter the distance in meters: "))

        # Dont allow 0 as input for the divisor since we cant divide by 0
        while time == 0:
            print("Time can't be 0")
            time = float(input("Enter the time in seconds: "))


        # Calculate the velocity
        velocity = distance / time

        # Print the result
        print("Velocity: " + str(velocity) + " m/s")

else:
    print("The input value was not valid.")