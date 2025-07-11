from dao.crops_dao import CropDAO

def afficher_cultures():
    crops = CropDAO.load_crops()
    for c in crops:
        machines = ", ".join(c.required_machines)
        print(f"🌾 {c.name} - Durée : {c.growth_time} jours - Rendement : {c.yield_per_field}L/ha")
        print(f"   Machines requises : {machines}\n")