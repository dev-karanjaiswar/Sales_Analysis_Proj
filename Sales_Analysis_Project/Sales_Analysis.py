import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\Karan\Desktop\Data_Science\Sales_Analysis_Project\mock_sales_data.csv")
print(df.isnull().sum())
# Since there are no null values, we proceed without filling and dropping any rows.

print(df.info())
# Since 'date' column is in string format (object) we will convert it.
df['date'] = pd.to_datetime(df['date'])

# Analytical Part 
df['Revenue'] = df['quantity'] * df['price']
print(df.info())

Shapes = df.shape

Columns = df.columns
 
head = df.head()

tail = df.tail()


# Region-wise analysis
# Region by revenue
region_revenue = df.groupby('region')['Revenue'].sum().sort_values(ascending=False)
#print("Region by revenue:\n", region_revenue)

#product-wise analysis
#product by revenue
product_revenue = df.groupby('product')['Revenue'].sum().sort_values(ascending=False)
#print("Product by revenue:\n", product_revenue)

df['month'] = df['date'].dt.to_period('M')

# Month wise analysis
# Month by revenue
month_revenue = df.groupby('month')['Revenue'].sum().sort_values(ascending=False)
#print("Month by revenue:\n", month_revenue)

higest_revenue_month = month_revenue.idxmax()
#print("Highest revenue month:", higest_revenue_month)

Lowest_revenue_month = month_revenue.idxmin()
#print("Lowest revenue month:", Lowest_revenue_month)

sns.set(style="whitegrid")

plt.figure(figsize=(8,5))
sns.barplot(x=region_revenue.index, y=region_revenue.values, color='green')

plt.title('Region-wise Revenue')
plt.xlabel('Region')
plt.ylabel('total Revenue (₹)')
plt.tight_layout()

#plt.savefig('region_wise_revenue.png')  
# plt.show()

plt.figure(figsize=(12,9))
sns.barplot(x=month_revenue.index, y=month_revenue.values, color='skyblue')

plt.title('Month-wise Revenue')
plt.xlabel('Month')
plt.ylabel('Total Revenue (₹)')
plt.tight_layout()

# plt.savefig('month_wise_revenue.png')
# plt.show()

# pie chart visulaization for product-wise revenue
plt.figure(figsize=(8, 8))
plt.pie(product_revenue, labels=product_revenue.index, autopct='%1.1f%%', startangle=140)
plt.title('Product-wise Revenue Distribution')
plt.axis('equal') 

plt.savefig('product_wise_revenue.png')
plt.show()