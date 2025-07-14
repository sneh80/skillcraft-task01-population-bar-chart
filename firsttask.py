import matplotlib.pyplot as plt

# Data
age_groups = ['0–20 years', '21–64 years', '65+ years']
population = [512, 807, 98]
percent = [36.1, 57.0, 6.9]

# Bar chart
plt.bar(age_groups, population, color=['gold', 'skyblue', 'violet'])

# Labels
plt.title("India's Population Distribution by Age (2022)")
plt.xlabel("Age Group")
plt.ylabel("Population (in millions)")

# Show percentage labels above bars
for i in range(len(age_groups)):
    plt.text(i, population[i] + 20, f"{percent[i]}%", ha='center', fontsize=10, fontweight='bold')

# Style
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

# Show the chart
plt.show()

