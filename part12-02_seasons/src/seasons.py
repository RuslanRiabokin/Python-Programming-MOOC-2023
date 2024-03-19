# Write your solution here:
def sort_by_seasons(items: list):
    def order_by_price(item: tuple):
        return item["seasons"]

    return sorted(items, key=order_by_price)
