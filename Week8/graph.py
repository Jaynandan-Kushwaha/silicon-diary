import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("pvt_summary.csv")

plt.figure()
plt.plot(df["PVT_CORNER"], df["WNS"])
plt.xticks(rotation=90)
plt.ylabel("WNS (ns)")
plt.title("Worst Negative Slack vs PVT")
plt.tight_layout()
plt.savefig("wns_plot.png")
plt.show()

plt.figure()
plt.plot(df["PVT_CORNER"], df["TNS"])
plt.xticks(rotation=90)
plt.ylabel("TNS (ns)")
plt.title("Total Negative Slack vs PVT")
plt.tight_layout()
plt.savefig("tns_plot.png")
plt.show()

