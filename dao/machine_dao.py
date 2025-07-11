from mongoDbDatabase import get_database
from farm import Machine

class MachineDAO:

    @staticmethod
    def save_machine(machine: Machine):
        db = get_database()
        machine_doc = {
            "name": machine.name,
            "total_units": machine.available_units
        }
        db.machines.insert_one(machine_doc)

    @staticmethod
    def load_machines() -> list[Machine]:
        db = get_database()
        machines = []
        for doc in db.machines.find():
            machine = Machine(name=doc["name"], total_units=doc["total_units"])
            machines.append(machine)
        return machines

    @staticmethod
    def update_machine_units(name: str, new_units: int):
        """Met à jour le nombre d'unités disponibles pour une machine donnée."""
        db = get_database()
        result = db.machines.update_one(
            {"name": name},
            {"$set": {"total_units": new_units}}
        )
        if result.matched_count == 0:
            print(f"⚠️ Aucun document trouvé pour la machine '{name}'")
        else:
            print(f"✅ Machine '{name}' mise à jour avec {new_units} unités")

    """def __init__(self, name: str, total_units: int):
        self.name = name
        self.available_units = total_units

    def __repr__(self):
        return f"Machine(name='{self.name}', units={self.available_units})"""
