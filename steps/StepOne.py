import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../airline_passenger_satisfaction.csv").set_index("ID")
#mean
means = df[["Departure Delay", "Arrival Delay"]].mean()
print(f'Mean | Depature Delay: {means[0]} | Arrival Delay: {means[1]}')
print("----------------------------------------------------------------------------")
print("mode")
modes = df[["Departure Delay", "Arrival Delay"]].mode(axis='rows')
print(modes)
print("----------------------------------------------------------------------------")
print("median")
medians = df[["Departure Delay", "Arrival Delay"]].median(axis='rows')
print(medians.transpose())
print("----------------------------------------------------------------------------")
print("Standard Deviation")
std = df[["Departure Delay", "Arrival Delay"]].std()
print(std)
print("----------------------------------------------------------------------------")
print("Percentiles")
tenth = df[["Departure Delay", "Arrival Delay"]].quantile(.1)
fifty = df[["Departure Delay", "Arrival Delay"]].quantile(.5)
sevfitth = df[["Departure Delay", "Arrival Delay"]].quantile(.75)
ninetieth = df[["Departure Delay", "Arrival Delay"]].quantile(.9)
print(tenth)
print(fifty)
print(sevfitth)
print(ninetieth)
print("----------------------------------------------------------------------------")
print("Quartiles")
first = df[["Departure Delay", "Arrival Delay"]].quantile(.25)
second = df[["Departure Delay", "Arrival Delay"]].quantile(.5)
third = df[["Departure Delay", "Arrival Delay"]].quantile(.75)
print(first)
print(second)
print(third)
print("----------------------------------------------------------------------------")
print("Skew")
Skew = df[["Departure Delay", "Arrival Delay"]].skew(axis=0)
print(Skew)
print("----------------------------------------------------------------------------")
print("Coverance")
Cover = df["Departure Delay"].cov(df["Arrival Delay"])
print(Cover)
print("----------------------------------------------------------------------------")
print("Correlation")
Corr = df["Departure Delay"].corr(df["Arrival Delay"])
print(Corr) 
#print(f'Mode | Depature Delay: {modes[0]} | Arrival Delay: {modes[1]}')
boxplot = df.boxplot(column=['Departure Delay'])
boxplot.plot()
plt.show()