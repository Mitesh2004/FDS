import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv(r'h:\archive\SOCR-HeightWeight.csv')

# Plot weight vs height
plt.figure(figsize=(8, 5))
plt.plot(df['Weight(Pounds)'], df['Height(Inches)'])
#plt.scatter(df['Weight(Pounds)'], df['Height(Inches)'])
plt.title('Weight vs Height')
plt.xlabel('Weight(Pounds)')
plt.ylabel('Height(Inches)')
plt.grid(True)
plt.show()