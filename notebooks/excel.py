import pandas as pd

data = {
    'Fund': ['Quant Mid Cap', 'Nippon Large Cap', 'SBI Small Cap', 'HDFC Money Market', 'Axis ELSS', 'Aditya Birla Banking'],
    'CAGR_5Y_%': [14.3, 13.5, 12.2, 6.8, 6.4, -4.0],
    'Risk_%': [1.10, 0.89, 0.87, 0.03, 0.85, 0.95],
    'Max_Fall_%': [-26.0, -15.4, -22.4, -0.2, -18.0, -35.0],
    'Verdict': ['Best Return, High Risk', 'Best Balanced', 'Good, High Risk', 'Safest, Low Return', 'Average', 'Avoid']
}
df = pd.DataFrame(data)
df.to_excel("Mutual_Fund_Dashboard.xlsx", index=False)
print("Excel ban gaya! Folder me check karo - Mutual_Fund_Dashboard.xlsx")