import numpy as np
customer_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
last_purchase_days_ago = np.array([5, 15, 20, 25, 30, 35, 40, 45, 50, 55])
recent_purchases = last_purchase_days_ago <= 30
no_recent_purchases = last_purchase_days_ago > 30
customers_recent = customer_ids[recent_purchases]
customers_no_recent = customer_ids[no_recent_purchases]
print("Active Customer(last purchase <= 30 days ago) :")
print(customers_recent)
print("Inactive Customer(Last Purchase > 30 days ago) :")
print(customers_no_recent)
