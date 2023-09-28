class Item:
    id: int
    price: float
    description: str

    def __init__(self, id: int, price: float, description: str):
        self.id = id
        self.price = price
        self.description = description

    def __str__(self):
        return {
            "id": self.id,
            "price": self.price,
            "description": self.description
        }
