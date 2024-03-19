# Write your solution here
def search(products: list, criterion: callable):
    return [product for product in products if criterion(product)]

# Example criterion function
def price_under_4_euros(product):
    return product[1] < 4
