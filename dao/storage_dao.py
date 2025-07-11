from mongoDbDatabase import get_database  
from farm import Storage

class StorageDAO:

    def load_storage(capacity=100) -> Storage:
        """Charge le contenu de stockage depuis la base."""
        db = get_database()
        storage = db.storage.find_one({"_id": "default"})
        if storage is None:
            # Si le stockage n'existe pas, on le crée avec la capacité par défaut
            storage = Storage(capacity=capacity)
            db.storage.insert_one({"_id": "default", "contents": storage.contents})
            return storage
        # Si le stockage existe, on le charge
        storage_contents = storage.get("contents", {})
        storage = Storage(capacity=capacity)
        storage.contents = storage_contents
        return storage



    def save_item_to_storage(item_name: str, qty: int):
        """Ajoute ou met à jour une ressource dans le stockage."""
        db = get_database()
        storage = db.storage.find_one({"_id": "default"})   
        if storage is None:
            # Si le stockage n'existe pas, on le crée
            storage = {"_id": "default", "contents": {}}
        else:
            storage = storage.get("contents", {})
        # Met à jour ou ajoute l'item dans le stockage
        storage[item_name] = storage.get(item_name, 0) + qty
        # Enregistre le stockage mis à jour
        db.storage.update_one({"_id": "default"}, {"$set": {"contents":
            storage}}, upsert=True)
        

    def add_item_to_storage(item_name: str, qty: int):
        """Ajoute une quantité d’un item dans le stockage.""" 
        db = get_database()
        storage = db.storage.find_one({"_id": "default"})
        if storage is None:
            # Si le stockage n'existe pas, on le crée
            storage = {"_id": "default", "contents": {}}
        else:
            storage = storage.get("contents", {})   
        # Met à jour ou ajoute l'item dans le stockage
        storage[item_name] = storage.get(item_name, 0) + qty
        # Enregistre le stockage mis à jour
        db.storage.update_one({"_id": "default"}, {"$set": {"contents": storage}}, upsert=True)
    


    def remove_item_from_storage(item_name: str, qty: int):
        """Enlève une quantité d’un item (si possible)."""
        db = get_database()
        storage = db.storage.find_one({"_id": "default"})
        if storage is None:
            # Si le stockage n'existe pas, on ne peut rien enlever
            return  
        storage_contents = storage.get("contents", {})
        if item_name not in storage_contents:
            # Si l'item n'existe pas dans le stockage, on ne peut rien enlever
            return
        current_qty = storage_contents[item_name]
        if current_qty < qty:
            # Si la quantité demandée est supérieure à la quantité disponible, on ne peut rien enlever
            return
        # Met à jour la quantité de l'item
        new_qty = current_qty - qty
        if new_qty > 0:
            storage_contents[item_name] = new_qty
        else:
            del storage_contents[item_name]

        # Enregistre le stockage mis à jour
        db.storage.update_one({"_id": "default"}, {"$set": {"contents":
            storage_contents}}, upsert=True)
        conn = get_database()
        # Si l'item a été complètement retiré, on le supprime du stockage   
        if new_qty == 0:
            db.storage.update_one({"_id": "default"}, {"$unset": {f"contents.{item_name}": ""}})
        conn.close()
      
