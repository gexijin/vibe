# CSV Descriptive Statistics

Generate simple descriptive statistics from a CSV file.

## Instructions

When this skill is invoked:

1. Ask the user for the path to the CSV file if not provided
2. Read the CSV file and identify:
   - Total number of rows and columns
   - Column names and their data types
   - For numeric columns, calculate:
     - Mean
     - Median
     - Standard deviation
     - Min and max values
     - Count of missing values
   - For categorical columns, calculate:
     - Unique value counts
     - Most frequent values (top 5)
     - Count of missing values

3. Present the statistics in a clear, organized format using markdown tables

4. If the CSV is very large (>1000 rows), warn the user and ask if they want to proceed with a sample or the full dataset

5. Handle common errors gracefully:
   - File not found
   - Invalid CSV format
   - Empty files
   - Permission issues

6. Use Python with pandas for the analysis - use the `mcp__ide__executeCode` tool to run the analysis

## Example output format

```
## CSV File Statistics

**File:** data.csv
**Rows:** 1000
**Columns:** 5

### Numeric Columns

| Column | Mean | Median | Std Dev | Min | Max | Missing |
|--------|------|--------|---------|-----|-----|---------|
| age    | 35.2 | 34.0   | 12.5    | 18  | 85  | 0       |
| score  | 78.5 | 80.0   | 15.2    | 0   | 100 | 5       |

### Categorical Columns

| Column | Unique Values | Top Value (Count) | Missing |
|--------|---------------|-------------------|---------|
| gender | 3             | Female (520)      | 2       |
| city   | 45            | New York (150)    | 0       |
```
