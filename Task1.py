import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('age_gender.csv')
plt.hist(df['age'], bins=10, color='lightgreen', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()