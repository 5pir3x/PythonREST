from flask import Blueprint, request
from Models.Item import Item
from Models.Store import Store
from db.db import stores

store_controller = Blueprint('store', __name__)


@store_controller.route("/stores", methods=["GET"])
def get_stores():
    stores2 = [store.__str__() for store in stores.values()]
    return {"stores": stores2}


@store_controller.route("/store", methods=["GET"])
def get_store():
    # Get the 'storeId' parameter from the URL query string
    try:
        store_id = int(request.args.get("storeId"))
    except TypeError:
        return {"message": "Missing parameter storeId"}, 400
    try:
        store = stores[store_id]
    except KeyError:
        return {"message": "Store not found"}, 404
    return store.__str__()


# works for JSON= {
# "id": 1,
# "items":
# [
#     {"description": "Huble bubble Test",
#      "id": 1,
#      "price": 10.1}
#     ,
#     { "description": "Chunga lunga TT",
#       "id": 2,
#       "price": 24.12}
# ]
# ,
# "name": "Kaja2"
# }
@store_controller.route("/store", methods=["POST"])
def add_store():
    body = request.get_json()
    listofItems: [Item] = [Item(item["id"], item["price"], item["description"]) for item in body["items"]]
    stores[body["id"]] = Store(body["id"], body["name"], listofItems)
    return stores[body["id"]].__str__()
