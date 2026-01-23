import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "day": [1, 2, 3, 4, 5],
    "hours_studied": [2, 3, 4, 5, 6],
    "score": [70, 75, 80, 85, 90]
}

df = pd.DataFrame(data)

average_score = df["score"].mean()
print("Average score:", average_score)


plt.plot(df["day"], df["score"])
plt.xlabel("Day")
plt.ylabel("Score")
plt.title("Score Over Time")
plt.show()
