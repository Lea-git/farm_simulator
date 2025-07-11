from mongoDbDatabase import get_database
from farm import CropType

class CropDAO:

    @staticmethod
    def load_crops() -> list[CropType]:
        db = get_database()
        crops = []

        for doc in db.crops.find():
            crop = CropType(
                name=doc["name"],
                growth_time=doc.get("growth_time", 0),
                yield_per_field=doc.get("yield_per_field", 0),
                required_machines=doc.get("required_machines", [])
            )
            crops.append(crop)

        return crops

    @staticmethod
    def save_crop(crop: CropType):
        db = get_database()
        doc = {
            "name": crop.name,
            "growth_time": crop.growth_time,
            "yield_per_field": crop.yield_per_field,
            "required_machines": crop.required_machines
        }
        db.crops.insert_one(doc)