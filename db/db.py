from Models.Item import Item
from Models.Store import Store
from flask_sqlalchemy import SQLAlchemy

item1 = Item(1, 20.1, "Huble bubble")
item2 = Item(2, 24.1, "Chunga lunga")

store1 = Store(23, "Pece", [item1])
store2 = Store(3, "Kaja", [item1, item2])

stores: dict[int, Store] = {
    store1.id: store1,
    store2.id: store2
}
db = SQLAlchemy()
