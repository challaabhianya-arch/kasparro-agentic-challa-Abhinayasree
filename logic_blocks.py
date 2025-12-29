class LogicBlocks:
    def build(self, product):
        return {
            "name": product.name,
            "ingredients": product.ingredients,
            "benefits": product.benefits,
            "usage": product.usage,
            "side_effects": product.side_effects,
            "price": product.price
        }

    def compare(self, product_a, product_b):
        return {
            "product_a": product_a,
            "product_b": product_b
        }
