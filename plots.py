import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


data = pd.read_excel("data/results.xlsx")

print(data)

freq = data.groupby('site').count()

print(freq)

