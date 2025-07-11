from dao.champs_dao import FieldDAO

def effectuer_action(champ_id: int, action: str) -> dict:
    champs = FieldDAO.load_fields()
    champ = next((c for c in champs if c.number == champ_id), None)
    if not champ:
        return {"status": "error", "message": f"Champ {champ_id} introuvable"}

    if action == "labourer":
        champ.state = "labouré"
    elif action == "semer":
        champ.state = "semé"
    elif action == "fertiliser":
        champ.state = "fertilisé"
    elif action == "récolter":
        champ.state = "récolté"
    elif action == "transporter":
        champ.state = "transporté"
    elif action == "transformer":
        champ.state = "transformé"
    else:
        return {"status": "error", "message": f"Action inconnue: {action}"}

    # Optionnel : sauvegarder la modification
    # FieldDAO.save_field(champ)

    return {
        "status": "success",
        "champ_id": champ.number,
        "nouvel_etat": champ.state
    }