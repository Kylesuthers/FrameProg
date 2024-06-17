import pandas as pd
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

xl1 = pd.read_csv(r"C:\Users\Kyle Suthers\OneDrive - Leeds Beckett University\Documents\csv\order (2) (2).csv")
xl2 = pd.read_csv(r"C:\Users\Kyle Suthers\OneDrive - Leeds Beckett University\Documents\csv\order_line (2) (2).csv")


#1
"""
city_orders = xl1['shipping_address_city'].value_counts()
city_orders_sorted = city_orders.sort_values(ascending=False)

print(city_orders_sorted)

#2
customer_orders = xl1['customer_id'].value_counts()
customer_orders_sorted = customer_orders.sort_values(ascending=False)

print(customer_orders_sorted)

#3
xl1['created_at'] = pd.to_datetime(xl1['created_at'])
xl1['closed_at'] = pd.to_datetime(xl1['closed_at'])
average_duration = (xl1['closed_at'] - xl1['created_at']).mean()
print(average_duration)






# sales forcast
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
"""
customer_orders = xl1['customer_id'].value_counts()
print(customer_orders)