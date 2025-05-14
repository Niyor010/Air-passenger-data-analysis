import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(df['Month'], df['Passengers'], marker='o')
plt.title("Monthly Air Passengers Over Time")
plt.xlabel("Month")
plt.ylabel("Number of Passengers")
plt.grid(True)
plt.show()