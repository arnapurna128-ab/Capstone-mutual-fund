import pandas as pd

df = pd.read_csv("data/processed/cleaned_nav.csv")
print("Total rows:", len(df))
print(df.head())

# Summary banao
summary = df.groupby('scheme_code')['nav'].agg(['count','mean','max','min']).round(2)
summary = summary.reset_index()
summary.columns = ['Scheme Code', 'Days', 'Avg NAV', 'Max NAV', 'Min NAV']

top = df.sort_values('nav', ascending=False).head(10)

# Excel banao - 3 Sheets
with pd.ExcelWriter("Mutual_Fund_Dashboard.xlsx", engine='openpyxl') as writer:
    summary.to_excel(writer, sheet_name='Summary', index=False)
    top.to_excel(writer, sheet_name='Top Funds', index=False)
    df.to_excel(writer, sheet_name='Full Data', index=False)

print("Dashboard ban gaya! Mutual_Fund_Dashboard.xlsx")