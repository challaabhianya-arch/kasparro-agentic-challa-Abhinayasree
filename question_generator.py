class QuestionGenerator:
    def generate(self, product):
        return {
            "questions": [
                f"What is {product.name}?",
                "Who can use this product?",
                "What are the benefits?",
                "How to use the product?",
                "Is it safe for sensitive skin?",
                "What is the price?",
                "Is it good for oily skin?"
            ]
        }
