--Muhammad Zain (sp23-bai-032) maintainer
-- Zaimal Zia (Sp23-bai-043) collaborator

class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")

        total_price = self.price * quantity

        if quantity < 10:
            return total_price  # No discount

        discount_rate = 0
        if 10 <= quantity < 100:
            discount_rate = 10  # 10% discount
        elif quantity >= 100:
            discount_rate = 20  # 20% discount

        discount = total_price * (discount_rate / 100)
        return total_price - discount

    def make_purchase(self, quantity):
        try:
            if quantity > self.amount:
                raise ValueError("Not enough stock to complete the purchase.")
            
            price = self.get_price(quantity)
            self.amount -= quantity

            print(f"Purchase successful!")
            print(f"Item: {self.name}")
            print(f"Quantity purchased: {quantity}")
            print(f"Total price charged: ${price:.2f}")
            print(f"Remaining stock: {self.amount}")
        except ValueError as e:
            print(f"Error: {e}")

# Example usage
product = Product("Diamond Nose Pin", 50, 31000)
product.make_purchase(2)  # Test purchase
