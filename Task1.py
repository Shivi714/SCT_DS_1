import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load CSV
df = pd.read_csv("Population.csv", delimiter=',')
df.columns = df.columns.str.strip()
df['Population 2024'] = pd.to_numeric(df['Population 2024'], errors='coerce')
df = df.dropna(subset=['Population 2024'])

# Top 20 countries
top20 = df.sort_values(by='Population 2024', ascending=False).head(20)

#  Generate 20 light colors from multiple pastel colormaps
pastel_colors = list(plt.cm.Pastel1(np.linspace(0, 1, 9))) + \
                list(plt.cm.Pastel2(np.linspace(0, 1, 8))) + \
                ['#fddde6', '#d0f0c0', '#fceabb']  # extra custom pastel shades

# Ensure we have exactly 20 colors
colors = pastel_colors[:20]

#  Plot
plt.figure(figsize=(12, 6))
plt.bar(top20['Country'], top20['Population 2024'], color=colors, edgecolor='black')
plt.title('Top 20 Countries by Population (2024)', fontsize=14)
plt.xlabel('Country')
plt.ylabel('Population')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()
