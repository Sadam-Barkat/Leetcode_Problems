## 2877. Create a DataFrame from List

### Problem Statement:
You are given a list of lists, where each inner list represents a row of data. Create a DataFrame using this list and set the appropriate headers (column names).

### Example:

#### Input:
```python
data = [[1, 'Alice', 25], [2, 'Bob', 30], [3, 'Charlie', 35]]
headers = ['ID', 'Name', 'Age']
Code to Create DataFrame:
python
Copy code
import pandas as pd

# List of lists
data = [[1, 'Alice', 25], [2, 'Bob', 30], [3, 'Charlie', 35]]

# Column headers
headers = ['ID', 'Name', 'Age']

# Create DataFrame
df = pd.DataFrame(data, columns=headers)

# Display DataFrame
print(df)
Output:
Copy code
   ID     Name  Age
0   1    Alice   25
1   2      Bob   30
2   3  Charlie   35
Explanation:
List of Lists: data represents the rows of the DataFrame.
Column Names: headers are the names for the columns.
Creating the DataFrame: pd.DataFrame(data, columns=headers) creates a DataFrame with the provided data and column names.
Diagram:
sql
Copy code
List of Lists:
    [
        [1, 'Alice', 25],    -> Row 1
        [2, 'Bob', 30],       -> Row 2
        [3, 'Charlie', 35]    -> Row 3
    ]

DataFrame Representation:
    +----+---------+-----+
    | ID |   Name  | Age |
    +----+---------+-----+
    |  1 |  Alice  |  25 |
    |  2 |   Bob   |  30 |
    |  3 | Charlie |  35 |
    +----+---------+-----+