import pandas as pd

# Load the summary results and compensation files
summary_df = pd.read_csv("summary_results.csv", index_col=0)
compensation_df = pd.read_csv("compensation_file.csv", header=None)

# Extract marker names and correction factors correctly
marker_names = compensation_df.iloc[0, :].str.strip()  # First row are marker names (including first column)
correction_factor_2 = compensation_df.iloc[1, :].astype(float)  # Second row contains correction factors

# Create a dictionary for easier lookup of correction factors
correction_factors_dict = dict(zip(marker_names, correction_factor_2))

# Ensure there are no leading or trailing spaces in summary_results column names
summary_df.columns = summary_df.columns.str.strip()

# Check if 'B_not_ALL' column exists
if "B_not_ALL" not in summary_df.columns:
    raise KeyError("Column 'B_not_ALL' not found in summary_results.csv")

# Filter markers in summary_df that match those in the compensation file
markers = [marker for marker in summary_df.columns if marker != "B_not_ALL"]

# Validate marker alignment
if not set(markers).issubset(correction_factors_dict):
    missing_markers = set(markers) - set(correction_factors_dict)
    raise ValueError(f"Mismatch: These markers are missing in the compensation file: {missing_markers}")

# Prepare a new DataFrame for compensated results
compensated_df = summary_df.copy()

# Apply the compensation formula to each marker value
for marker in markers:
    compensated_df[marker] = summary_df.apply(
        lambda row: row[marker] - row["B_not_ALL"] * correction_factors_dict[marker],
        axis=1
    )

# Save the compensated results to a new CSV file
compensated_df.to_csv("compensated_file.csv")

print("Compensated file created successfully.")
