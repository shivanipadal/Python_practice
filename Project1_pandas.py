import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\\Users\\shivani.padal\\Downloads\\movies_complete.csv", parse_dates=['release_date'])

df_best = df[["poster_path", "title", "budget_musd", "revenue_musd",
              "vote_count", "vote_average", "popularity"]].copy()

df_best['profit_musd'] = df.revenue_musd.sub(df.budget_musd)
df_best['return'] = df.revenue_musd.divide(df.budget_musd)

print(list(df_best))
