import csv
import random
from datetime import datetime, timedelta

# Function to generate a random order number
def generate_order_number():
    return f"ORD-{random.randint(1000, 9999)}"

# Function to generate a random date between 2022-01-01 and 2023-06-30
def generate_random_date():
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2023, 6, 30)
    days_difference = (end_date - start_date).days
    random_days = random.randint(0, days_difference)
    return start_date + timedelta(days=random_days)

# Generate 100 rows of CSV data
data = []
for i in range(100, 200):
    #order_number = generate_order_number()
    order_number = "ord_0000000" + str(i)
    customer = random.choice(['长沙凡绣', '江苏海港', '深证一锋', '常州芳莱', '北京压压', '南京里德', '绍兴欧绣'])
    order_meters = random.randint(1, 100)
    order_amount = random.randint(100000, 300000)
    product_name = random.choice(['牛仔布', '麻布', '棉布', '红布', '蓝布', '羽绒'])
    order_date = generate_random_date().strftime('%Y-%m-%d')
    deposit = order_amount * 0.05
    received_amount = random.uniform(0.5, 1) * order_amount
    cost = random.uniform(0.5, 0.8) * order_amount
    gross_profit = order_amount - cost

    row = [order_number, customer, order_meters, order_amount, product_name, order_date,
           deposit, received_amount, cost, gross_profit]
    data.append(row)

# Write data to CSV file
csv_file = "orders_data1.csv"
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["订单号", "客户", "订单米数", "订单金额", "产品名称", "订单日", "定金", "已收金额", "成本", "毛利"])
    writer.writerows(data)

print(f"{len(data)}条CSV数据已生成并保存到 {csv_file}")

