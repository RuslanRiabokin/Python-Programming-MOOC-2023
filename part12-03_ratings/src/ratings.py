# TEE RATKAISUSI TÄHÄN:
def sort_by_ratings(items: list):
    def order_by_price(item: tuple):
        return item["rating"]

    return sorted(items, key=order_by_price, reverse=True)
