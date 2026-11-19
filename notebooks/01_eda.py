import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/live_nav.csv")
df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')
df = df.sort_values(['scheme_name','date'])
cutoff = df['date'].max() - pd.DateOffset(years=5)
df5 = df[df['date'] >= cutoff].copy()

print("RISK ANALYSIS - Kaunsa fund kitna hilta hai?")
print("="*50)
for name, group in df5.groupby('scheme_name'):
    group = group.copy()
    group['daily_return'] = group['nav'].pct_change() * 100
    risk = group['daily_return'].std()
    peak = group['nav'].cummax()
    drawdown = ((group['nav'] - peak) / peak * 100).min()
    cagr = (((group.iloc[-1]['nav'] / group.iloc[0]['nav']) ** (1/5)) - 1) * 100
    print(f"{name[:30]}")
    print(f"  CAGR: {cagr:.1f}% | Risk (Daily up-down): {risk:.2f}% | Sabse zyada gira: {drawdown:.1f}%")