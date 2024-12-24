## 2881. Create a New Column

### Problem Statement:
Given a DataFrame, create a new column based on an existing column or a condition. This can be done using various methods such as direct assignment, applying functions, or using conditions.

### Code:
```python
import pandas as pd

# Create a sample DataFrame
data = {
    'ID': [101, 102, 103, 104],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Salary': [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)

# Create a new column 'Bonus' based on 'Salary' column
df['Bonus'] = df['Salary'] * 0.1

# Display the result
print(df)
Testcase 1:
Input:
python
Copy code
data = {
    'ID': [101, 102, 103, 104],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Salary': [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)
Create new column 'Bonus' as 10% of 'Salary':
Expected Output:
yaml
Copy code
    ID     Name  Salary  Bonus
0  101    Alice   50000  5000.0
1  102      Bob   60000  6000.0
2  103  Charlie   70000  7000.0
3  104    David   80000  8000.0
Testcase 2:
Input:
python
Copy code
data = {
    'Product': ['Apple', 'Banana', 'Cherry', 'Date'],
    'Price': [1.2, 0.5, 3.5, 2.8]
}
df = pd.DataFrame(data)
Create new column 'Discount' as 20% of 'Price':
Expected Output:
mathematica
Copy code
   Product  Price  Discount
0   Apple    1.2      0.24
1  Banana    0.5      0.10
2  Cherry    3.5      0.70
3    Date    2.8      0.56
Test Result:
Example 1:
For the DataFrame:

markdown
Copy code
    ID     Name  Salary
0  101    Alice   50000
1  102      Bob   60000
2  103  Charlie   70000
3  104    David   80000
After creating the new column Bonus as 10% of Salary, the result is:

yaml
Copy code
    ID     Name  Salary  Bonus
0  101    Alice   50000  5000.0
1  102      Bob   60000  6000.0
2  103  Charlie   70000  7000.0
3  104    David   80000  8000.0
Example 2:
For the DataFrame:

mathematica
Copy code
   Product  Price
0   Apple    1.2
1  Banana    0.5
2  Cherry    3.5
3    Date    2.8
After creating the new column Discount as 20% of Price, the result is:

mathematica
Copy code
   Product  Price  Discount
0   Apple    1.2      0.24
1  Banana    0.5      0.10
2  Cherry    3.5      0.70
3    Date    2.8      0.56