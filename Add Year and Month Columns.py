df['Year'] = df['Month'].dt.year
df['Month_Name'] = df['Month'].dt.strftime('%b')  
df['Month_Num'] = df['Month'].dt.month            
yearly_avg = df.groupby('Year')['Passengers'].mean()
print(yearly_avg)