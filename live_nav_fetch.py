import requests
import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

schemes = {
    125497: "HDFC_Top_100_Direct",
    119551: "SBI_Bluechip",
    120503: "ICICI_Bluechip",
    118632: "Nippon_Large_Cap",
    119092: "Axis_Bluechip",
    120841: "Kotak_Bluechip"
}

all_data = []

for code, name in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"
    print(f"Fetching {name} ({code})...")
    response = requests.get(url)
    data = response.json()
    fund_name = data['meta']['scheme_name']
    nav_list = data['data']
    for row in nav_list:
        all_data.append({
            'scheme_code': code,
            'scheme_name': fund_name,
            'date': row['date'],
            'nav': float(row['nav'])
        })
    print(f"Done {name}")

df = pd.DataFrame(all_data)
df.to_csv("data/raw/live_nav.csv", index=False)
print("Ho gaya! live_nav.csv ban gayi")
print(df.shape)