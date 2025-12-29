from models import Product

class DataParser:
    def parse(self, data):
        return Product(
            name=data["name"],
            ingredients=data["ingredients"],
            benefits=data["benefits"],
            usage=data["usage"],
            side_effects=data["side_effects"],
            price=data["price"]
        )
