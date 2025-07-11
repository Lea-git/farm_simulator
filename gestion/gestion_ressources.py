from dao.machine_dao import MachineDAO
from dao.storage_dao import StorageDAO
from dao.usine_dao import UsineDAO
from dao.crops_dao import CropDAO

class RessourceManager:

    @staticmethod
    def verifier_disponibilite_machine(nom_machine: str, minimum: int = 1) -> bool:
        machines = MachineDAO.load_machines()
        for m in machines:
            if m.name == nom_machine and m.available_units >= minimum:
                return True
        return False

    @staticmethod
    def verifier_stock(item: str, quantite_requise: int) -> bool:
        stocks = StorageDAO.load_storage()
        for s in stocks:
            if s.item == item and s.quantity >= quantite_requise:
                return True
        return False

    @staticmethod
    def verifier_usine_ready(output: str) -> dict:
        factories = UsineDAO.load_factories()
        for f in factories:
            if f.output_type == output:
                intrants = f.input_type
                statut = all(RessourceManager.verifier_stock(item, 1) for item in intrants)
                return {
                    "usine": f.output_type,
                    "intrants": intrants,
                    "production_possible": statut
                }
        return {"usine": output, "intrants": [], "production_possible": False}

    @staticmethod
    def analyser_cycle_culture(culture_nom: str) -> dict:
        crops = CropDAO.load_crops()
        for crop in crops:
            if crop.name == culture_nom:
                machines_dispo = all(RessourceManager.verifier_disponibilite_machine(m, 1) for m in crop.required_machines)
                return {
                    "culture": crop.name,
                    "machines_requises": crop.required_machines,
                    "machines_disponibles": machines_dispo,
                    "rendement_attendu": crop.yield_per_field
                }
        return {
            "culture": culture_nom,
            "machines_requises": [],
            "machines_disponibles": False,
            "rendement_attendu": 0
        }