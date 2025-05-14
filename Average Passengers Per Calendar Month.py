monthly_avg = df.groupby('Month_Num')['Passengers'].mean()
monthly_avg.index = pd.to_datetime(monthly_avg.index, format='%m').month_name()
print(monthly_avg)
