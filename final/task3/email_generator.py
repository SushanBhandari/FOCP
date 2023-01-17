import sys
import random

def generate_email(id, name):
  # Split name into two parts
  name_parts = name.split(" ")
  if len(name_parts) < 2:
    print(f"Error: Invalid name format for ID {id}: {name}")
    return 
  first_name = name_parts[0].strip()
  last_name = name_parts[-1].strip()
  # Remove any non-alphabetic characters from the last name
  last_name = "".join(c for c in last_name if c.isalpha())
  initial = first_name[0]
  digits = "".join(str(random.randint(0, 9)) for _ in range(4))
  # Return the email
  return f"{id} {initial.lower()}.{last_name.lower()}{digits}@poppleton.ac.uk" "\n"

# Check if the command-line argument is provided
if len(sys.argv) < 2:
  print("Error: Missing command-line argument.")
  sys.exit(1)

# Try to open the file
try:
  with open(sys.argv[1], "r") as f:
    # Read the lines from the file
    lines = f.readlines()
except IOError:
  print(f"Error: Cannot open {sys.argv[1]}. Sorry about that.")
  sys.exit(1)

# Create a list of emails
emails = [generate_email(line.split()[0], "  ".join(line.split()[1:])) for line in lines if line.strip()]

#Makes a file name emails
with open("emails.txt", "w") as f:
  f.writelines(emails)
