## 2880. Select Data

### Problem Statement:
Given a DataFrame, select data based on specific conditions or criteria. The selection can be done using column values, conditions, or other criteria for extracting the required rows and columns.

### Code:
```python
import pandas as pd

# Create a sample DataFrame
data = {
    'ID': [101, 102, 103, 104],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)

# Select rows where ID is 101 and columns ID, Name, and Salary
selected_data = df[df['ID'] == 101][['ID', 'Name', 'Salary']]

# Display the result
print(selected_data)
Testcase 1:
Input:
python
Copy code
data = {
    'ID': [101, 102, 103, 104],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)
Condition: df['ID'] == 101
Expected Output:
markdown
Copy code
    ID   Name  Salary
0  101  Alice   50000
Testcase 2:
Input:
python
Copy code
data = {
    'Product': ['Apple', 'Banana', 'Cherry', 'Date'],
    'Price': [1.2, 0.5, 3.5, 2.8],
    'Quantity': [10, 20, 15, 30]
}
df = pd.DataFrame(data)
Condition: df['Price'] > 2.0
Expected Output:
mathematica
Copy code
   Product  Price  Quantity
2  Cherry    3.5        15
3    Date    2.8        30
Test Result:
Example 1:
For the DataFrame:

Copy code
   ID     Name  Age  Salary
0  101    Alice   25   50000
1  102      Bob   30   60000
2  103  Charlie   35   70000
3  104    David   40   80000
After applying the condition df['ID'] == 101, the selected data is:

markdown
Copy code
    ID   Name  Salary
0  101  Alice   50000
Example 2:
For the DataFrame:

mathematica
Copy code
   Product  Price  Quantity
0   Apple    1.2        10
1  Banana    0.5        20
2  Cherry    3.5        15
3    Date    2.8        30
After applying the condition df['Price'] > 2.0, the selected data is:

mathematica
Copy code
   Product  Price  Quantity
2  Cherry    3.5        15
3    Date    2.8        30