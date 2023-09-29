from db.db import db


class StoreEntity(db.Model):
    __tablename__ = "STORES"

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.Float(precision=2), unique=False, nullable=False)
    items = db.relationship("ItemEntity", back_populates="store", lazy="dynamic")
    # description = db.Column(db.String(80), unique=True, nullable=False)