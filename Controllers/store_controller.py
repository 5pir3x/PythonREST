from flask import Blueprint, request, jsonify

from Entities import StoreEntity, ItemEntity
from Models.Item import Item
from Models.Store import Store
from db.db import stores, db

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
    listOfItems: [Item] = [Item(item["id"], item["price"], item["description"]) for item in body["items"]]
    stores[body["id"]] = Store(body["id"], body["name"], listOfItems)
    return stores[body["id"]].__str__()

# Should work for JSON:
#     {
#         "id": 1,
#         "name": "Example Store",
#         "items": [
#             {
#                 "id": 1,
#                 "price": 10.99,
#                 "description": "Item 1",
#                 "store_id": 1
#             },
#             {
#                 "id": 2,
#                 "price": 15.99,
#                 "description": "Item 2",
#                 "store_id": 1
#             }
#         ]
#     }

@store_controller.route("/addStore", methods=["POST"])
def add_store_to_db():
    try:
        # Parse the JSON data from the request
        data = request.get_json()

        # Create a new StoreEntity instance
        store = StoreEntity(
            id=data["id"],
            name=data["name"]
        )

        # Create ItemEntity instances and associate them with the store
        if "items" in data:
            for item_data in data["items"]:
                item = ItemEntity(
                    id=item_data["id"],
                    price=item_data["price"],
                    description=item_data["description"],
                    store=store  # Associate the item with the store
                )
                db.session.add(item)  # Add the item to the session

        db.session.add(store)  # Add the store to the session
        db.session.commit()  # Commit changes to the database

        return jsonify({"message": "Store added successfully", "store_id": store.id}), 201  # 201 Created
    except Exception as e:
        # Handle any exceptions (e.g., validation errors) here
        return jsonify({"error": str(e)}), 400  # 400 Bad Request


@store_controller.route("/store", methods=["DELETE"])
def delete_store():
    # Get the 'storeId' parameter from the URL query string
    try:
        store_id = int(request.args.get("storeId"))
    except TypeError:
        return {"message": "Missing parameter storeId"}, 400
    try:
        del stores[store_id]
    except KeyError:
        return {"message": "Store not found"}, 404
    return {f"message": f"Store with id={store_id} has been deleted"}
