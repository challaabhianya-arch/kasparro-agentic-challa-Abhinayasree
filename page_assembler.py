import json, os

class PageAssembler:
    def save(self, filename, data):
        os.makedirs("outputs", exist_ok=True)
        with open(f"outputs/{filename}", "w") as f:
            json.dump(data, f, indent=2)
