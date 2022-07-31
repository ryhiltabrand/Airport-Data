import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../airline_passenger_satisfaction.csv").set_index("ID")

a24 = df.apply(lambda x: 1 if x['Satisfaction'] == "Neutral or Dissatisfied" else 4, axis = 1)
result = pd.concat([df, a24], axis=1)
result.to_csv("A24.csv")
print(result)