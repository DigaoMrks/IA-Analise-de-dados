# -*- coding: utf-8 -*-


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:\Users\Digão\Downloads\InsectSprays.csv'; sep=',')

df.boxplot()
plt.show()