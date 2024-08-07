import numpy as np
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2, 4.0, 7.0, 45.0, -4.0, -12.0])
hot_days = temperatures > 35
cold_days = temperatures < 5
hot_day_indices = np.where(hot_days)[0]
cold_day_indices = np.where(cold_days)[0]
days = np.arange(1, len(temperatures) + 1)
print("Hot Days:")
for idx in hot_day_indices:
    print(f"Day {days[idx]}: Temperature = {temperatures[idx]}°C")
print("\nCold Days:")
for idx in cold_day_indices:
    print(f"Day {days[idx]}: Temperature = {temperatures[idx]}°C")
