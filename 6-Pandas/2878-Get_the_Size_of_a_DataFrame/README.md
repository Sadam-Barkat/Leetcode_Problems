## 2878. Get the Size of a DataFrame

### Problem Statement:
Given a DataFrame, determine its size (the number of elements it contains). The size is the total number of rows multiplied by the total number of columns.

### Code:
```python
import pandas as pd

# Create a sample DataFrame
data = {'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# Get the size of the DataFrame
size = df.size

# Display the size
print("Size of the DataFrame:", size)
Testcase 1:
Input:
python
Copy code
data = {'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
Expected Output:
yaml
Copy code
Size of the DataFrame: 9
Testcase 2:
Input:
python
Copy code
data = {'Product': ['Apple', 'Banana'], 'Price': [1.2, 0.5], 'Quantity': [10, 20]}
df = pd.DataFrame(data)
Expected Output:
yaml
Copy code
Size of the DataFrame: 6
Test Result:
Example 1:
For the DataFrame:

Copy code
   ID     Name  Age
0   1    Alice   25
1   2      Bob   30
2   3  Charlie   35
The size is 3 rows * 3 columns = 9 elements.

Example 2:
For the DataFrame:

mathematica
Copy code
   Product  Price  Quantity
0   Apple    1.2        10
1  Banana    0.5        20
The size is 2 rows * 3 columns = 6 elements.

Explanation:
df.size returns the total number of elements in the DataFrame, calculated as the product of the number of rows and columns.