import pandas as pd
import matplotlib.pyplot as plt

# Sample data (list of ages)
ages = [21, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

# Create a DataFrame
data = pd.DataFrame({'Age': ages})

# Explore the data
print(data.describe())

# Visualize the distribution of ages
plt.hist(data['Age'], bins=5, edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.show()
