class TemplateEngine:
    def apply(self, page_type, content):
        return {
            "page_type": page_type,
            "data": content
        }
