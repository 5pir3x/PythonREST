from db.db import db


class ItemEntity(db.Model):
    __tablename__ = "ITEMS"

    id: int = db.Column(db.Integer, primary_key=True)
    price: float = db.Column(db.Float(precision=2), unique=False, nullable=False)
    description: str = db.Column(db.String(80), unique=True, nullable=False)
    store_id: int = db.Column(db.Integer, db.ForeignKey("STORES.id"), unique=False, nullable=False)
    store = db.relationship("StoreEntity", back_populates="items")
