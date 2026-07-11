import pandas as pd
import numpy as np
from functools import wraps
import matplotlib.pyplot as plt

# Decorator for logging
def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}...")
        return func(*args, **kwargs)
    return wrapper

class SalesAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = self.load_data()

    @log_action
    def load_data(self):
        return pd.read_csv(self.file_path)

    @log_action
    def calculate_metrics(self):
        total_sales = self.df['amount'].sum()
        avg_sales = self.df['amount'].mean()
        top_products = self.df.groupby('product')['amount'].sum().nlargest(5)
        top_customers = self.df.groupby('customer')['amount'].sum().nlargest(5)
        return {
            'total_sales': total_sales,
            'avg_sales': avg_sales,
            'top_products': top_products,
            'top_customers': top_customers
        }

    @log_action
    def monthly_trend(self):
        self.df['date'] = pd.to_datetime(self.df['date'])
        monthly_sales = self.df.groupby(pd.Grouper(key='date', freq='M'))['amount'].sum()
        return monthly_sales

    @log_action
    def export_report(self, metrics):
        with pd.ExcelWriter('sales_report.xlsx') as writer:
            metrics['top_products'].to_excel(writer, sheet_name='Top Products')
            metrics['top_customers'].to_excel(writer, sheet_name='Top Customers')
            monthly_sales = self.monthly_trend()
            monthly_sales.to_excel(writer, sheet_name='Monthly Trend')

    def run(self):
        metrics = self.calculate_metrics()
        print("Sales Metrics:")
        print(f"Total Sales: {metrics['total_sales']}")
        print(f"Average Sales: {metrics['avg_sales']}")
        print("Top Products:\n", metrics['top_products'])
        print("Top Customers:\n", metrics['top_customers'])
        self.export_report(metrics)

# Usage
analyzer = SalesAnalyzer('sales_data.csv')
analyzer.run()