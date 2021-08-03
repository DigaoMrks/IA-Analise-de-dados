import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# GRÁFICO 1
df_data = {'idades': ['Old', 'Young'],
           'pumpkin': [10, 5],
           'apple': [10, 5]}

x = df_data['pumpkin']
y = df_data['apple']


bar_1 = x
bar_2 = y


x_pos = np.arange(len(bar_1))

first_bar = plt.bar(x_pos, bar_1, 0.90, color='pink')
second_bar = plt.bar(x_pos, bar_2, 0.90, color='red', bottom=bar_1)

plt.xticks(x_pos+0.25, df_data['idades'])
plt.title('Grafico 1')
plt.ylabel('Count')
plt.xlabel('Age')
plt.legend((first_bar[0], second_bar[0]), ('Apple', 'Pumpkin'), title = "Flavour", bbox_to_anchor=(1.4, 0.5), loc='center right', ncol=1)
plt.show()


# GRÁFICO 2

df_data = {'idades': ['Old', 'Young'],
           'pumpkin': [7, 11],
           'apple': [11, 7]}

x = df_data['pumpkin']
y = df_data['apple']


bar_1 = x
bar_2 = y


x_pos = np.arange(len(bar_1))

first_bar = plt.bar(x_pos, bar_1, 0.90, color='pink')
second_bar = plt.bar(x_pos, bar_2, 0.90, color='red', bottom=bar_1)

plt.xticks(x_pos+0.25, df_data['idades'])
plt.title('Grafico 2')
plt.ylabel('Count')
plt.xlabel('Age')
plt.legend((first_bar[0], second_bar[0]), ('Apple', 'Pumpkin'), title = "Flavour", bbox_to_anchor=(1.4, 0.5), loc='center right', ncol=1)
plt.show()


#  GRÁFICO 3
df_data = {'idades': ['Old', 'Young'],
           'pumpkin': [10, 10],
           'apple': [8, 2]}

x = df_data['pumpkin']
y = df_data['apple']


bar_1 = x
bar_2 = y


x_pos = np.arange(len(bar_1))

first_bar = plt.bar(x_pos, bar_1, 0.90, color='pink')
second_bar = plt.bar(x_pos, bar_2, 0.90, color='red', bottom=bar_1)

plt.xticks(x_pos+0.25, df_data['idades'])
plt.title('Grafico 3')
plt.ylabel('Count')
plt.xlabel('Age')
plt.legend((first_bar[0], second_bar[0]), ('Apple', 'Pumpkin'), title = "Flavour", bbox_to_anchor=(1.4, 0.5), loc='center right', ncol=1)
plt.show()