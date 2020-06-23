from models.store import StoreModel
from flask_restful import Resource

class Store(Resource):
    def get(self,name):
        store = StoreModel.get_by_name(name)
        if store:
            return store.json()
        return {"message": "Store not found"},404

    def post(self,name):
        if StoreModel.get_by_name(name):
            return {"message": "Store with the name '{}' already exists".format(name)},400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return{"message": "An error occured while creating store"}, 500
        return store.json(), 201

    def delete(self,name):
        store = StoreModel.get_by_name(name)
        if store:
            store.delete_from_db()
        return {"message": "Store deleted."}            


class StoreList(Resource):
    def get(self):
        return {"stores": [store.json() for store in StoreModel.query.all()]}