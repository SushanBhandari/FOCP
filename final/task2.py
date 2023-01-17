# Initialize variables
runners = 0
total_time = 0
fastest_time = float('inf')
slowest_time = 0
fastest_runner = ""
runner_numbers = []  # Add a list to track the runner numbers

# Read input from the user
print("Park Run Timer\n~~~~~~~~~~~~~~\n\nLet's go!")
while True:
    data = input(">")
    if data.upper() == 'END':
        # If the input is END,end exit the loop
        break
    items = data.split('::')

    # Check if the input got three digits or not
    if len(items) !=2:
        print("Error in data stream. Ignorning. Carry on.")
        continue

    try:
        # converting the runner number and time to integers
        runner_number = int(items[0])
        time = int(items[1])

        
        if time < 0:
            print("Error: Time cannot be negative. Ignoring this input.")
            continue
        
        # Check if the runner number is repeated
        if runner_number in runner_numbers:
            print("Error: Runner number has already been entered. Ignoring this input.")
            continue

    except ValueError:
        # If the conversion fails, ignore this input
        continue

    runner_numbers.append(runner_number)

    runners += 1
    total_time += time
    if time < fastest_time:
        fastest_time = time
        fastest_runner = runner_number
    if time > slowest_time:
        slowest_time = time

# Calculate the average time in minutes and seconds
if runners == 0:
    print("No data found. Nothing to do. What a pity.")
else:
    average_time = total_time / runners
    minutes, seconds = divmod(average_time, 60)

    fastest_minutes, fastest_seconds = divmod(fastest_time, 60)

    slowest_minutes, slowest_seconds = divmod(slowest_time, 60)

    # Print the results
    print(f"\n Total Runners: {runners}")
    if minutes == 1:
        print(f"Average Time:  {int(minutes)} minute, {int(seconds)} seconds")
    else:
        print(f"Average Time:  {int(minutes)} minutes, {int(seconds)} seconds")
    if fastest_minutes == 1:
        print(f"Fastest Time:  {int(fastest_minutes)} minute, {int(fastest_seconds)} seconds")
        
    else:
        print(f"Fastest Time:  {int(fastest_minutes)} minutes, {int(fastest_seconds)} seconds")
        
    if slowest_time==1:
        print(f"Slowest Time:  {int(slowest_minutes)} minute,  {int(slowest_seconds)} second")
    else:
        print(f"Slowest Time:  {int(slowest_minutes)} minutes, {int(slowest_seconds)} seconds")



    print(f"Best Time Here: Runner #{fastest_runner}")
