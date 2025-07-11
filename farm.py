from enum import Enum
from typing import List, Dict


class FieldState(Enum):
    RECOLTE = "récolté"
    LABOURE = "labouré"
    SEME = "semé"
    FERTILISE = "fertilisé"
    PRET_A_RECOLTER = "prêt à récolter"


class CropType:
    def __init__(self, name: str, growth_time: int, yield_per_field: int):
        self.name = name
        self.growth_time = growth_time
        self.yield_per_field = yield_per_field


class Field:
    def __init__(self, number: int, lot: int = None):
        self.number = number
        self.state = FieldState.RECOLTE
        self.crop_type: CropType = None
        self.lot = lot

    def update_state(self, new_state: FieldState):
        self.state = new_state


class Machine:
    def __init__(self, name: str, total_units: int):
        self.name = name
        self.available_units = total_units

    def use(self) -> bool:
        if self.available_units > 0:
            self.available_units -= 1
            return True
        return False

    def release(self):
        self.available_units += 1


class Storage:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.contents: Dict[str, int] = {}

    def has_space_for(self, qty: int) -> bool:
        return self.current_load() + qty <= self.capacity

    def current_load(self) -> int:
        return sum(self.contents.values())

    def add(self, item: str, qty: int) -> bool:
        if self.has_space_for(qty):
            self.contents[item] = self.contents.get(item, 0) + qty
            return True
        return False


class Factory:
    def __init__(self, input_type: str, output_type: str, multiplier: float):
        self.input_type = input_type
        self.output_type = output_type
        self.multiplier = multiplier

    def transform(self, storage: Storage, input_qty: int) -> bool:
        if storage.contents.get(self.input_type, 0) >= input_qty:
            output_qty = int(input_qty * self.multiplier)
            if storage.has_space_for(output_qty - input_qty):
                storage.contents[self.input_type] -= input_qty
                storage.add(self.output_type, output_qty)
                return True
        return False


class Player:
    def __init__(self, name: str):
        self.name = name
        self.fields: List[Field] = []
        self.machines: Dict[str, Machine] = {}
        self.storage = Storage(capacity=100)
        self.factories: List[Factory] = []

    def add_field(self, field: Field):
        self.fields.append(field)

    def add_machine(self, machine: Machine):
        self.machines[machine.name] = machine

    def add_factory(self, factory: Factory):
        self.factories.append(factory)

    def find_machine(self, machine_name: str) -> Machine:
        return self.machines.get(machine_name)

    def labour_field(self, field: Field) -> bool:
        plow = self.find_machine("Charrue")
        if field.state == FieldState.RECOLTE and plow and plow.use():
            field.update_state(FieldState.LABOURE)
            plow.release()
            return True
        return False

    def seed_field(self, field: Field, crop: CropType) -> bool:
        seeder = self.find_machine("Semeuse")
        if field.state == FieldState.LABOURE and seeder and seeder.use():
            field.crop_type = crop
            field.update_state(FieldState.SEME)
            seeder.release()
            return True
        return False

    def fertilize_field(self, field: Field) -> bool:
        fert = self.find_machine("Fertilisateur")
        if field.state == FieldState.SEME and fert and fert.use():
            field.update_state(FieldState.FERTILISE)
            fert.release()
            return True
        return False

    def prepare_for_harvest(self, field: Field):
        if field.state == FieldState.FERTILISE:
            field.update_state(FieldState.PRET_A_RECOLTER)

    def harvest_field(self, field: Field) -> bool:
        harvester = self.find_machine("Moissonneuse")
        if field.state == FieldState.PRET_A_RECOLTER and harvester and harvester.use():
            crop = field.crop_type
            qty = crop.yield_per_field
            if self.storage.add(crop.name, qty):
                field.crop_type = None
                field.update_state(FieldState.RECOLTE)
                harvester.release()
                return True
        return False

    def transform(self, factory: Factory, input_qty: int) -> bool:
        return factory.transform(self.storage, input_qty)


# ----------------- Simulation Demo -----------------

if __name__ == "__main__":
    player = Player("Alice")

    # Ajouter les machines
    player.add_machine(Machine("Charrue", 2))
    player.add_machine(Machine("Semeuse", 2))
    player.add_machine(Machine("Fertilisateur", 2))
    player.add_machine(Machine("Moissonneuse", 2))

    # Définir une culture
    ble = CropType("Blé", growth_time=3, yield_per_field=10)

    # Créer un champ
    champ1 = Field(number=1)
    player.add_field(champ1)

    # Ajouter une usine
    moulin = Factory("Blé", "Farine", multiplier=0.8)
    player.add_factory(moulin)

    # Simuler le cycle complet
    print("🚜 Labourer :", player.labour_field(champ1), champ1.state.name)
    print("🌱 Semer :", player.seed_field(champ1, ble), champ1.state.name)
    print("💧 Fertiliser :", player.fertilize_field(champ1), champ1.state.name)
    player.prepare_for_harvest(champ1)
    print("⏳ Prêt à récolter :", champ1.state.name)
    print("🌾 Récolter :", player.harvest_field(champ1), champ1.state.name)
    print("📦 Stock :", player.storage.contents)
    print("🏭 Transformation :", player.transform(moulin, input_qty=5))
    print("📦 Stock après transformation :", player.storage.contents)
