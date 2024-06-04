import os
import pandas as pd

# Get the current working directory (where the script is executed)
current_directory = os.getcwd()

# Create an empty DataFrame to hold the combined data
combined_df = pd.DataFrame()

# Iterate over all folders in the current directory
for folder in os.listdir(current_directory):
    folder_path = os.path.join(current_directory, folder)

    if os.path.isdir(folder_path):  # Ensure it is a directory
        # Iterate over all files in the company directory
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)

            if os.path.isfile(file_path) and file.endswith(
                ".csv"
            ):  # Ensure it is a CSV file
                # Read the CSV file into a DataFrame
                df = pd.read_csv(file_path)

                # Add a new column for the company name
                df["Company"] = folder

                # Append the data to the combined DataFrame
                combined_df = pd.concat([combined_df, df], ignore_index=True)

# Define the output file path
output_file = os.path.join(current_directory, "combined_file.csv")

# Save the combined DataFrame to a new CSV file
combined_df.to_csv(output_file, index=False)

print(f"All files have been combined into {output_file}.")
