import os
import shutil

# Get the current working directory (where the script is executed)
current_directory = os.getcwd()

# Get the name of the script file
script_file = os.path.basename(__file__)

# List all files in the current directory
files = os.listdir(current_directory)

# Iterate over each file
for file in files:
    if (
        os.path.isfile(file) and file != script_file
    ):  # Ensure it is a file and not the script itself
        # Split the filename to extract the company name
        company_name = file.split("_")[0]

        # Create the company directory if it doesn't exist
        company_directory = os.path.join(current_directory, company_name)
        if not os.path.exists(company_directory):
            os.makedirs(company_directory)

        # Move the file to the respective company directory
        shutil.move(file, os.path.join(company_directory, file))

print("Files have been organized into their respective company folders.")
