import pandas as pd

df = pd.read_csv("data/processed/cleaned_nav.csv")
print("Total rows:", len(df))

# Summary
summary = df.groupby('scheme_code')['nav'].agg(['count','mean','max','min']).round(2)
summary = summary.reset_index()
summary.columns = ['Scheme Code', 'Days', 'Avg NAV', 'Max NAV', 'Min NAV']

top = df.sort_values('nav', ascending=False).head(10)

# Tumhara Comparison Table
data = {
    'Fund': ['Quant Mid Cap', 'Nippon Large Cap', 'SBI Small Cap', 'HDFC Money Market', 'Parag Parikh Flexi', 'Axis Small Cap'],
    'CAGR_5Y_%': [14.3, 13.5, 12.2, 6.8, 6.4, -4.0],
    'Risk_%': [1.10, 0.89, 0.87, 0.03, 0.85, 0.95],
    'Max_Fall_%': [-26.0, -15.4, -22.4, -0.2, -18.0, -35.0],
    'Verdict': ['Best Return, High Risk', 'Best Balanced', 'Good, High Risk', 'Safest, Low Return', 'Good Balanced', 'High Risk']
}
compare = pd.DataFrame(data)

# Naya naam - purani file se ladai nahi hogi
with pd.ExcelWriter("Dashboard_v2.xlsx", engine='openpyxl') as writer:
    summary.to_excel(writer, sheet_name='Summary', index=False)
    top.to_excel(writer, sheet_name='Top Funds', index=False)
    compare.to_excel(writer, sheet_name='Comparison', index=False)
    df.to_excel(writer, sheet_name='Full Data', index=False)

print("Excel ban gaya! Folder me check karo - Dashboard_v2.xlsx")