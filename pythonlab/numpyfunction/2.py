import numpy as np
monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])
quarterly_sales = np.array_split(monthly_sales, 4)
quarterly_sales = np.vstack(quarterly_sales)
print("Quarterly Sales Data:",quarterly_sales)
