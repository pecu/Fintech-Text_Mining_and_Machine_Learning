import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

original_data = pd.read_csv(sys.argv[1]).drop(columns=["label_headers"]).values.flatten()
data = [i for i in original_data if i < 0]

_, axs=plt.subplots()
#cumulative = -1 if all i in data > 0; otherwise, cumulative = 1
axs.hist(data, bins = 20, cumulative = 1, edgecolor='black', density=True)
axs.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(xmax=1))
plt.show()

