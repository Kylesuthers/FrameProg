import pandas as pd
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

xl1 = pd.read_csv(r"C:\Users\Kyle Suthers\OneDrive - Leeds Beckett University\Documents\csv\order (2) (2).csv")

date_col = next((col for col in xl1.columns if 'created_at' in col.lower()), None)
if date_col:
    xl1[date_col] = pd.to_datetime(xl1[date_col])
    xl1.set_index(date_col, inplace=True)

if 'total_price' in xl1.columns:
    monthly_sales = xl1.groupby(pd.Grouper(freq='M'))['total_price'].sum().reset_index()
else:
    print("'total_price' column not found in the xl1 DataFrame")

train_data = monthly_sales['total_price'].values

model = SimpleExpSmoothing(train_data)

fitted_model = model.fit()

forecast_months = pd.to_datetime('2022-09-30').to_period('M') - monthly_sales['created_at'].dt.to_period('M').max()

forecasts = fitted_model.forecast(forecast_months.n)

forecast_september_2022 = forecasts[-1]

print('Forecasted total_price for September 2022:', forecast_september_2022)