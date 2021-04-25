import plotly.figure_factory as ff
from random import randint
import pandas as pd
import statistics

df = pd.read_csv("csv/data.csv")

# I have taken no. of claps in the data

data = df["claps"].tolist()

population_mean = statistics.mean(data)
population_stdev = statistics.stdev(data)

print(f"Population Mean is: {population_mean}")
print(f"Standard Deviation Population is: {population_stdev}")


def takeSamples(no_of_samples):
    dataset = []
    for i in range(no_of_samples):
        random_index = randint(0, len(data))
        value = data[random_index]
        dataset.append(value)
    sample_mean = statistics.mean(dataset)
    return sample_mean


mean_list = []

for i in range(100):
    set_of_means = takeSamples(30)
    mean_list.append(set_of_means)

fig = ff.create_distplot([mean_list], ["Claps"], show_hist=False)
fig.show()

sample_mean = statistics.mean(mean_list)
sample_stdev = statistics.stdev(mean_list)

print(f"Sampling Mean is: {sample_mean}")
print(f"Standard Deviation is: {sample_stdev}")
