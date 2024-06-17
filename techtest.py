import pandas as pd

xl1 = pd.read_csv(r"C:\Users\Kyle Suthers\OneDrive - Leeds Beckett University\Documents\csv\order (2) (2).csv")
xl2 = pd.read_csv(r"C:\Users\Kyle Suthers\OneDrive - Leeds Beckett University\Documents\csv\order_line (2) (2).csv")

city_orders = xl1['shipping_address_city'].value_counts()
city_orders_sorted = city_orders.sort_values(ascending=False)

print(city_orders_sorted)

customer_orders = xl1['customer_id'].value_counts()
customer_orders_sorted = customer_orders.sort_values(ascending=False)

print(customer_orders_sorted)

xl1['created_at'] = pd.to_datetime(xl1['created_at'])
xl1['closed_at'] = pd.to_datetime(xl1['closed_at'])
average_duration = (xl1['closed_at'] - xl1['created_at']).mean()
print(average_duration)

customer_orders = xl1['customer_id'].value_counts()
print(customer_orders)

