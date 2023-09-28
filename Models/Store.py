from Models.Item import Item


class Store:
    id: int
    name: str
    items: [Item] = []

    def __init__(self, id: int, name: str, items: [Item]):
        self.id = id
        self.name = name
        self.items = []
        for item in items:
            self.items.append(item.__str__())

    def __str__(self):
        return {
            self.id: {
                "id": self.id,
                "name": self.name,
                "items": self.items
            }
        }

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "items": [self.items]
        }
