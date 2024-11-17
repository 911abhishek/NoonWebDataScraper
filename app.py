import pandas as pd


data = pd.read_csv("scrapeNoon\Extractions.csv")

print("-------------------------------------------------------------------------------")
data['Price'] = pd.to_numeric(data['Price'], errors='coerce')
most_expensive = data.loc[data['Price'].idxmax()]
cheapest = data.loc[data['Price'].idxmin()]

print(f"Most Expensive Product: {most_expensive['Name']} - ${most_expensive['Price']}")
print(f"Cheapest Product: {cheapest['Name']} - ${cheapest['Price']}")
products_per_brand = data['Brand'].value_counts()
products_per_seller = data['Brand'].value_counts()

print("\nNumber of Products from Each Brand:")
print(products_per_brand)
print("\nNumber of Products by Each Seller (using Brand):")
print(products_per_seller)
