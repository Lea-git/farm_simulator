from dao.machine_dao import MachineDAO
from dao.usine_dao import UsineDAO

def main():
    machine_dao = MachineDAO()
    machines = machine_dao.load_machines()
    print("Machines :", machines)

    usine_dao = UsineDAO()
    usines = usine_dao.load_factories()
    print("Usines :", usines)

if __name__ == "__main__":
    main()
"""
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
print(client.list_database_names())  # Trouve ta base
db = client["ferme"]
print(db.list_collection_names()) 

print(db.ferme.count_documents({}))   # Vérifie qu'elle contient 'factories'
db.factories.find_one()"""


from gestion.gestion_champs import afficher_champs
from gestion.gestion_machines import afficher_machines
from gestion.gestion_usines import afficher_usines

afficher_champs()
afficher_machines()
afficher_usines()
