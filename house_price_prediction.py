import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("house_prices.csv")

plt.scatter(data["Size"], data["Price"])

plt.title("House Size vs Price")
plt.xlabel("Size")
plt.ylabel("Price")

plt.show()