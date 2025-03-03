# Compensation Script

## Overview
This Python script reads a CSV file (`summary_results.csv`) containing sample data with marker values and a correction factor (`B_not_ALL`). It also reads another CSV file (`compensation_file.csv`) containing additional correction factors for each marker. The script applies a compensation formula to adjust the marker values and outputs the corrected data into `compensated_file.csv`.

## Compensation Formula
For each marker:
```
corrected_value = original_value - (B_not_ALL * correction_factor_2)
```
where:
- `original_value` is the marker value from `summary_results.csv`
- `B_not_ALL` is the correction factor from `summary_results.csv`
- `correction_factor_2` is retrieved from `compensation_file.csv`

## File Formats
### 1. `summary_results.csv`
- First row: Marker names
- First column: Sample names
- Other columns: Values for each marker
- Last column: `B_not_ALL` correction factor

#### Example:
| Sample  | Marker1 | Marker2 | B_not_ALL |
|---------|---------|---------|-----------|
| Sample1 | 10.5    | 8.2     | 0.05      |
| Sample2 | 12.3    | 7.8     | 0.07      |

### 2. `compensation_file.csv`
- First row: Marker names
- Second row: Correction factors (`correction_factor_2`)

#### Example:
| Marker1 | Marker2 |
|---------|---------|
| 0.02    | 0.03    |

## Usage
### Prerequisites
Ensure you have Python installed along with the required libraries:
```sh
pip install pandas
```

### Running the Script
```sh
python compensation.py
```

### Output File: `compensated_file.csv`
- Same structure as `summary_results.csv`
- Marker values are adjusted using the compensation formula

## Troubleshooting
### Common Errors & Fixes
1. **KeyError: 'B_not_ALL'**
   - Ensure `B_not_ALL` column exists in `summary_results.csv`.
   - Check for typos in the column name.

2. **ValueError: Mismatch between marker names in files**
   - Verify that marker names in `compensation_file.csv` match those in `summary_results.csv`.

3. **TypeError: unsupported operand type(s) for -: 'str' and 'float'**
   - Ensure all values in `summary_results.csv` are numeric.
   - The script automatically converts values to numeric, but check for unexpected text in the files.


