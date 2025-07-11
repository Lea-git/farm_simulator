from dao.champs_dao import FieldDAO

def afficher_champs():
    fields = FieldDAO.load_fields()
    for field in fields:
        crop = field.crop_type.name if field.crop_type else "Aucune culture"
        print(f"Champ #{field.number} - Lot {field.lot} - État: {field.state.name} - Culture: {crop}")