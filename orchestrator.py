from data_parser import DataParser
from question_generator import QuestionGenerator
from logic_blocks import LogicBlocks
from template_engine import TemplateEngine
from page_assembler import PageAssembler

PRODUCT_A = {
    "name": "GlowBoost Vitamin C Serum",
    "ingredients": ["Vitamin C", "Hyaluronic Acid"],
    "benefits": ["Brightening", "Fades dark spots"],
    "usage": "Apply 2–3 drops in the morning before sunscreen",
    "side_effects": "Mild tingling for sensitive skin",
    "price": "₹699"
}

PRODUCT_B = {
    "name": "ClearSkin Vitamin Serum",
    "ingredients": ["Vitamin C"],
    "benefits": ["Skin glow"],
    "usage": "Apply once daily",
    "side_effects": "None",
    "price": "₹899"
}

def run():
    parser = DataParser()
    product_a = parser.parse(PRODUCT_A)
    product_b = PRODUCT_B

    qna = QuestionGenerator().generate(product_a)
    logic = LogicBlocks()

    engine = TemplateEngine()
    assembler = PageAssembler()

    faq = engine.apply("FAQ_PAGE", qna)
    product_page = engine.apply("PRODUCT_PAGE", logic.build(product_a))
    comparison = engine.apply("COMPARISON_PAGE", logic.compare(PRODUCT_A, PRODUCT_B))

    assembler.save("faq.json", faq)
    assembler.save("product_page.json", product_page)
    assembler.save("comparison_page.json", comparison)

if __name__ == "__main__":
    run()
