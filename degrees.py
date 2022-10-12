import os
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st


df_degrees = pd.read_csv(os.path.join("Resources", "degrees-that-pay-back.csv"))
print(df_degrees.head())

df_college = pd.read_csv(os.path.join("Resources", "salaries-by-college-type.csv"))

df_region = pd.read_csv(os.path.join("Resources", "salaries-by-region.csv"))

print(df_college.head())