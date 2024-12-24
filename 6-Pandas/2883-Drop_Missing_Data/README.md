# 2883. Drop Missing Data

## Problem Statement

In pandas, missing data is often represented by `NaN` (Not a Number) or `None`. To ensure the accuracy and integrity of our dataset, it's crucial to handle missing data. One common approach is to **drop the rows or columns** that contain missing data.

## Functionality

Use the `dropna()` method in pandas to drop missing data (i.e., rows or columns that contain `NaN` or `None`).

### Code Example

```python
import pandas as pd
import numpy as np

# Sample DataFrame with missing values
data = {'student_id': [355, 951, 470, 977, 300],
        'name': [None, None, 'Quincy', 'Sophia', 'Liam'],
        'age': [9, 8, 20, None, 15]}

df = pd.DataFrame(data)

# Drop rows with any missing values
df_cleaned = df.dropna()

# Drop columns with any missing values
df_cleaned_columns = df.dropna(axis=1)

print("DataFrame after dropping rows with missing values:")
print(df_cleaned)

print("\nDataFrame after dropping columns with missing values:")
print(df_cleaned_columns)
Output
sql
Copy code
DataFrame after dropping rows with missing values:
   student_id    name   age
2          470  Quincy  20.0
4          300    Liam  15.0

DataFrame after dropping columns with missing values:
   student_id
0          355
1          951
2          470
3          977
4          300