def make_purchase(self, quantity):
      
      try:
        if quantity > self.amount:
            raise ValueError("Not enough stock to complete the purchase.")
        price = self.get_price(quantity)
        print('Total price charged: ', price)
        self.amount -= quantity
      except ValueError as e:
            print(f"Error: {e}")