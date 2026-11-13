import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# ==========================================
# SELF-ASSESSMENT REFLECTIONS (Lab 15)
# 1. Clear titles, labeled axes, and distinct colors make charts immediately 
#    readable within 10 seconds without needing the underlying data table.
# 2. Example context statement: "The South region drove $45,000 in revenue, 
#    which is 25% above the regional average."
# 3. This lab successfully connects data cleaning to visual storytelling, 
#    acting as a great dress rehearsal for the final capstone.
# ==========================================

# Load cleaned data
df = pd.read_csv('data/clean_sales.csv')

# Calculate revenue if it doesn't exist yet
if 'revenue' not in df.columns:
  df['revenue'] = df['unit_price'] * df['quantity_sold']
  
df['order_date'] = pd.to_datetime(df['order_date'])

# EXERCISE 1: Revenue by region (Bar Chart)
print('--- EXERCISE 1: REVENUE BY REGION ---')
region_rev = df.groupby('region')['revenue'].sum().reset_index()
region_rev = region_rev.sort_values(by='revenue', ascending=False)

plt.figure(figsize=(8, 5))
plt.bar(
    region_rev['region'],
    region_rev['revenue'],
    color=['skyblue', 'salmon', 'lightgreen', 'orange'],
)
plt.title('Total Revenue by Region')
plt.xlabel('Region')
plt.ylabel('Revenue ($)')
plt.savefig('charts/q1_revenue_by_region.png')
plt.close()
print(
    f"Top region: {region_rev.iloc[0]['region']} with $"
    f"{region_rev.iloc[0]['revenue']:.2f}"
)

# EXERCISE 2: Monthly revenue trend (Line Chart)
print('\n--- EXERCISE 2: MONTHLY REVENUE TREND ---')
df['month'] = df['order_date'].dt.month
monthly_rev = df.groupby('month')['revenue'].sum().reset_index()

plt.figure(figsize=(9, 5))
plt.plot(
    monthly_rev['month'],
    monthly_rev['revenue'],
    marker='o',
    color='b',
    linestyle='-',
)
plt.title('Monthly Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.xticks(range(1, 13))
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig('charts/q2_monthly_trend.png')
plt.close()
print('Monthly trend chart saved successfully.')

# EXERCISE 3: Order size distribution (Histogram)
print('\n--- EXERCISE 3: ORDER SIZE DISTRIBUTION ---')
plt.figure(figsize=(8, 5))
plt.hist(df['revenue'], bins=20, color='purple', edgecolor='black')
plt.title('Order Size Distribution')
plt.xlabel('Revenue ($)')
plt.ylabel('Frequency')
plt.savefig('charts/q3_order_distribution.png')
plt.close()

mean_rev = df['revenue'].mean()
median_rev = df['revenue'].median()
print(f'Mean revenue: ${mean_rev:.2f}, Median revenue: ${median_rev:.2f}')
# Distribution is right-skewed because the mean is higher than the median due to high-value outliers.

# EXERCISE 4: Custom business question (Revenue by Product Category)
print('\n--- EXERCISE 4: CUSTOM BUSINESS QUESTION ---')
cat_rev = df.groupby('product_category')['revenue'].sum().reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(
    data=cat_rev,
    x='product_category',
    y='revenue',
    hue='product_category',
    palette='viridis',
    legend=False,
)
plt.title('Total Revenue by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Revenue ($)')
plt.savefig('charts/q4_custom.png')
plt.close()
print('Custom product category chart saved successfully.')

# EXERCISE 6: Multiple aggregations using .agg()
print('\n--- EXERCISE 6: MULTIPLE AGGREGATIONS ---')
agg_df = df.groupby('region').agg(
    total_revenue=('revenue', 'sum'), order_count=('revenue', 'count')
)
agg_df['avg_order_value'] = agg_df['total_revenue'] / agg_df['order_count']
print(agg_df)