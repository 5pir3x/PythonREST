from flask import Blueprint, request, jsonify

from db.db import stores

store_controller = Blueprint('store', __name__)


@store_controller.route("/stores", methods=["GET"])
def get_stores():
    stores2 = {store.id: store.to_dict() for store in stores.values()}
    return {"stores": stores2}


@store_controller.route("/store", methods=["GET"])
def get_store():
    # Get the 'storeId' parameter from the URL query string
    store_id = int(request.args.get("storeId"))
    if store_id is None:
        return {"message": "Missing parameter storeId"}, 400
    else:
        try:
            store = stores[store_id]
        except KeyError:
            return {"message": "Store not found"}, 404
    return {"store": store.__str__()}
