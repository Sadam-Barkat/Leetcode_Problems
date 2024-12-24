## 2879. Display the First Three Rows

### Problem Statement:
Given a DataFrame, display the first three rows of the dataset.

### Code:
```python
import pandas as pd

# Create a sample DataFrame
data = {'ID': [1, 2, 3, 4, 5], 'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'], 'Age': [25, 30, 35, 40, 45]}
df = pd.DataFrame(data)

# Display the first three rows
first_three_rows = df.head(3)

# Display the result
print(first_three_rows)
Testcase 1:
Input:
python
Copy code
data = {'ID': [1, 2, 3, 4, 5], 'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'], 'Age': [25, 30, 35, 40, 45]}
df = pd.DataFrame(data)
Expected Output:
Copy code
   ID     Name  Age
0   1    Alice   25
1   2      Bob   30
2   3  Charlie   35
Testcase 2:
Input:
python
Copy code
data = {'Product': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'], 'Price': [1.2, 0.5, 3.5, 2.8, 4.0], 'Quantity': [10, 20, 15, 30, 50]}
df = pd.DataFrame(data)
Expected Output:
mathematica
Copy code
   Product  Price  Quantity
0   Apple    1.2        10
1  Banana    0.5        20
2  Cherry    3.5        15
Test Result:
Example 1:
For the DataFrame:

Copy code
   ID     Name  Age
0   1    Alice   25
1   2      Bob   30
2   3  Charlie   35
3   4    David   40
4   5      Eva   45
The first three rows are:

Copy code
   ID     Name  Age
0   1    Alice   25
1   2      Bob   30
2   3  Charlie   35
Example 2:
For the DataFrame:

mathematica
Copy code
   Product  Price  Quantity
0   Apple    1.2        10
1  Banana    0.5        20
2  Cherry    3.5        15
3    Date    2.8        30
4  Elderberry 4.0       50
The first three rows are:

mathematica
Copy code
   Product  Price  Quantity
0   Apple    1.2        10
1  Banana    0.5        20
2  Cherry    3.5        15
Explanation:
df.head(3) returns the first three rows of the DataFrame.
You can adjust the number inside head() to get a different number of rows if needed.