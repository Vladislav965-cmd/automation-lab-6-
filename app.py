def order_total(price, quantity, discount_percent=0):
    if price < 0 or quantity < 0:
        raise ValueError("price and quantity must be non-negative")
    if not 0 <= discount_percent <= 100:
        raise ValueError("discount must be between 0 and 100")
    total = price * quantity
    return round(total * (100 - discount_percent) / 100, 2)


if __name__ == "__main__":
    print(order_total(250, 4, 10))
