import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("   POPULATION DATA ANALYTICS 2025   ")

print("Loading dataset...")
df = pd.read_csv('dataset.csv', thousands=',')
df.columns = df.columns.str.strip() 

df.rename(columns={'Population (2024)': 'Population (2025)'}, inplace=True)

output_dir = os.environ.get("OUTPUT_DIR", "output_graphs")
os.makedirs(output_dir, exist_ok=True)

print(f"\nOutput directory set to: {output_dir}")

print("\n[1] TOP 10 MOST POPULATED COUNTRIES:")
top_10_pop = df.nlargest(10, 'Population (2025)')
print(top_10_pop[['Country', 'Population (2025)']].to_string(index=False))

print("\n[2] TOP 5 LARGEST COUNTRIES BY LAND AREA (Km2):")
top_5_area = df.nlargest(5, 'Land Area (Km²)')
print(top_5_area[['Country', 'Land Area (Km²)']].to_string(index=False))

print("\n[3] QUICK STATISTICS:")
print(f"- Total Countries Analyzed: {len(df)}")
print(f"- Average Population Density: {df['Density (P/Km²)'].mean():.0f} people per Km2")

print("\nGenerating 5 visual graphs...")

# Graph 1
plt.figure(figsize=(12, 6))
sns.barplot(data=top_10_pop, x='Country', y='Population (2025)', hue='Country', palette='viridis', legend=False)
plt.title('Top 10 Most Populated Countries (2025)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, '1_vertical_bar_chart.png'))
plt.clf()

# Graph 2
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Land Area (Km²)', y='Population (2025)', alpha=0.6, color='blue')
plt.title('Population vs. Land Area')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, '2_scatter_plot.png'))
plt.clf()

# Graph 3
plt.figure(figsize=(10, 6))
sns.histplot(df['Density (P/Km²)'], bins=30, kde=True, color='orange')
plt.title('Distribution of Population Density')
plt.xlim(0, 1500)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, '3_histogram.png'))
plt.clf()

# Graph 4
plt.figure(figsize=(12, 6))
sns.barplot(data=df.nlargest(10, 'Land Area (Km²)'), x='Land Area (Km²)', y='Country', hue='Country', palette='magma', legend=False)
plt.title('Top 10 Largest Countries by Land Area')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, '4_horizontal_bar_chart.png'))
plt.clf()

# Graph 5
plt.figure(figsize=(8, 8))
top_5 = df.nlargest(5, 'Population (2025)')
other_pop = df['Population (2025)'].sum() - top_5['Population (2025)'].sum()
labels = top_5['Country'].tolist() + ['Rest of the World']
sizes = top_5['Population (2025)'].tolist() + [other_pop]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('Global Population Distribution (2025)')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, '5_pie_chart.png'))
plt.clf()

print("\nVERIFICATION: Graphs generated:")
for file in os.listdir(output_dir):
    print(f"   -> {file}")

print("\nTask Complete. Container shutting down.")