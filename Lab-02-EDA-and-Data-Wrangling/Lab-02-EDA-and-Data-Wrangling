import pandas as pd 
  
data = { 
    "Name": ["Asha", "Ravi", "Meera", "Karan"], 
    "Marks": [88, 72, 91, 65], 
    "Branch": ["CSE", "ECE", "CSE", "ISE"] 
} 
  
df = pd.DataFrame(data) 
 
print("\n--- Pandas DataFrame ---") 
print(df) 
  
print("\n--- Column Indexing ---") 
 
print("Name Column:") 
print(df["Name"]) 
 
print("\nMarks Column:") 
print(df["Marks"]) 
  
print("\n--- Row Indexing ---") 
 
print("First Row:") 
print(df.iloc[0]) 
 
print("\nThird Row:") 
print(df.iloc[2]) 
  
print("\n--- Specific Value ---") 
 
print("Marks of first student:", df.iloc[0, 1]) # 14. DataFrame Row Slicing 
 
print("\n--- Row Slicing ---") 
 
print("First two rows:") 
print(df.iloc[0:2]) 
  
print("\n--- Row and Column Slicing ---") 
 
print("First three rows with Name and Marks:") 
print(df.iloc[0:3, [0, 1]]) 
  
print("\n--- Data Filtering ---") 
 
result = df[df["Marks"] > 70] 
 
print("Students with Marks greater than 70:") 
print(result)
