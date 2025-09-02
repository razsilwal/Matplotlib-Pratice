import pandas as pd
import matplotlib.pyplot as plt


plt.style.use("fivethirtyeight")

data = pd.read_csv("2019-05-31-data.csv")

view_count = data["view_count"]
likes = data["likes"]
ratio = data["ratio"]

print(plt.colormaps())

plt.scatter(view_count, likes, c = ratio, cmap="RdYlBu_r", edgecolors= "black", linewidths=1, alpha=0.7)

cbar = plt.colorbar()
cbar.set_label("Like / Dislike Ratio")

plt.xscale("log")
plt.yscale("log")

plt.title("Trending Youtube Videos")
plt.xlabel("View Count")
plt.ylabel("Total Likes")

plt.tight_layout()
plt.show()