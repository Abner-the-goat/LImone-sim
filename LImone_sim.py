import random
import statistics
import matplotlib.pyplot as plt

# Parameters
p = 0.0025  # 0.25% chance per restock
restock_interval_minutes = 5
simulations = 10000  # number of simulated players

def simulate_one():
    """Simulate waiting for one King Limone appearance."""
    count = 0
    while True:
        count += 1
        if random.random() < p:
            return count

# Run simulations
results = [simulate_one() for _ in range(simulations)]

# Convert to hours (5 minutes per restock)
hours_waited = [r * restock_interval_minutes / 60 for r in results]

# Compute statistics
mean_hours = statistics.mean(hours_waited)
median_hours = statistics.median(hours_waited)
percentile_90 = statistics.quantiles(hours_waited, n=100)[89]

# Plot histogram
plt.hist(hours_waited, bins=50, color="#66cc66", edgecolor="black")
plt.title("Simulated Wait Time for King Limone Appearance (10,000 Trials)")
plt.xlabel("Hours Until King Limone Appears")
plt.ylabel("Number of Simulations")
plt.show()

print(f"Average wait time: {mean_hours:.2f} hours")
print(f"Median wait time: {median_hours:.2f} hours")
print(f"90th percentile (long waits): {percentile_90:.2f} hours")
