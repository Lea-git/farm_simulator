from dao.machine_dao import MachineDAO

def afficher_machines():
    machines = MachineDAO.load_machines()
    for machine in machines:
        print(f"{machine.name} : {machine.available_units} unités")

def modifier_unites_machine(nom_machine: str, nouvelles_unites: int):
    MachineDAO.update_machine_units(nom_machine, nouvelles_unites)