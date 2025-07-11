from dao.usine_dao import UsineDAO

def afficher_usines():
    factories = UsineDAO.load_factories()
    for factory in factories:
        intrants = ", ".join(factory.input_type)
        print(f"Usine - Produit : {factory.output_type} | Intrants : {intrants} | x{factory.multiplier}")