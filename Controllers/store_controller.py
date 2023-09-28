from flask import Blueprint

store_controller = Blueprint('store', __name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 10
            },
            {
                "name": "Chair2",
                "price": 102
            }
        ]
    }
]


@store_controller.route("/store", methods=["GET"])
def get_stores():
    return {"stores": stores}
