from mongoDbDatabase import get_database
from farm import Field, FieldState, CropType

class FieldDAO:

    @staticmethod
    def save_field(field: Field):
        """Ajoute un champ dans MongoDB."""
        db = get_database()
        field_doc = {
            "number": field.number,
            "state": field.state.name,
            "crop_type": field.crop_type.name if field.crop_type else None,
            "lot": field.lot
        }
        db.fields.insert_one(field_doc)

    @staticmethod
    def load_fields() -> list[Field]:
        """Charge tous les champs depuis MongoDB."""
        db = get_database()
        fields = []

        for doc in db.fields.find():
            f = Field(number=doc["number"], lot=doc["lot"])
            f.state = FieldState[doc["state"]]
            if doc.get("crop_type"):
                # 🚧 Temporaire : données fictives à remplacer par un chargement réel du CropType
                f.crop_type = CropType(name=doc["crop_type"], growth_time=3, yield_per_field=10)
            fields.append(f)

        return fields