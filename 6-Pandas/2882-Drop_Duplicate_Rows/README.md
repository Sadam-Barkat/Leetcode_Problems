## 2882. Drop Duplicate Rows

### Problem Statement:
Given a DataFrame, remove the rows that are exact duplicates. This operation will drop rows where all column values are identical to another row in the DataFrame.

### Code:
```python
import pandas as pd

# Create a sample DataFrame
data = {
    'ID': [101, 102, 103, 101],
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice'],
    'Salary': [50000, 60000, 70000, 50000]
}
df = pd.DataFrame(data)

# Drop duplicate rows
df = df.drop_duplicates(keep=False)

# Display the result
print(df)
Testcase 1:
Input:
python
Copy code
data = {
    'ID': [101, 102, 103, 101],
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice'],
    'Salary': [50000, 60000, 70000, 50000]
}
df = pd.DataFrame(data)
Remove duplicate rows (all columns must match):
Expected Output:
markdown
Copy code
    ID     Name  Salary
1  102      Bob   60000
2  103  Charlie   70000
Testcase 2:
Input:
python
Copy code
data = {
    'Product': ['Apple', 'Banana', 'Cherry', 'Apple'],
    'Price': [1.2, 0.5, 3.5, 1.2]
}
df = pd.DataFrame(data)
Remove duplicate rows (all columns must match):
Expected Output:
mathematica
Copy code
   Product  Price
1  Banana    0.5
2  Cherry    3.5
Test Result:
Example 1:
For the DataFrame:

markdown
Copy code
    ID     Name  Salary
0  101    Alice   50000
1  102      Bob   60000
2  103  Charlie   70000
3  101    Alice   50000
After removing duplicate rows, the result is:

markdown
Copy code
    ID     Name  Salary
1  102      Bob   60000
2  103  Charlie   70000
Example 2:
For the DataFrame:

mathematica
Copy code
   Product  Price
0   Apple    1.2
1  Banana    0.5
2  Cherry    3.5
3   Apple    1.2
After removing duplicate rows, the result is:

mathematica
Copy code
   Product  Price
1  Banana    0.5
2  Cherry    3.5