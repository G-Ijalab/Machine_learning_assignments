import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "C:/Users/balaj/OneDrive/Desktop/ml/assn1/dataset2.csv" # Update the file path as needed
data = pd.read_csv(file_path)

# Convert 'Date' to datetime format for time series analysis
data['Date'] = pd.to_datetime(data['Date'])
# Setting the aesthetic style of the plots
sns.set_style("whitegrid")

# 1. Sales distribution across different branches
plt.figure(figsize=(10, 6))
sns.barplot(x='Branch', y='Total', data=data.groupby('Branch')['Total'].sum().reset_index(),
palette='coolwarm')
plt.title('Sales Distribution Across Different Branches')
plt.xlabel('Branch')
plt.ylabel('Total Sales')
plt.show()

# 2. Comparison of gross income across product lines
plt.figure(figsize=(12, 7))
sns.barplot(x='gross income', y='Product line', data=data.groupby('Product line')['gross income'].sum().reset_index(), palette='viridis')
plt.title('Comparison of Gross Income Across Product Lines')
plt.xlabel('Gross Income')
plt.ylabel('Product Line')
plt.show()

# 3. Distribution of purchases between genders
plt.figure(figsize=(8, 8))
data['Gender'].value_counts().plot.pie(autopct='%1.1f%%', startangle=140,colors=['#ff9999','#66b3ff'], explode=(0.1, 0))
plt.title('Distribution of Purchases Between Genders')
plt.ylabel('')
plt.show()