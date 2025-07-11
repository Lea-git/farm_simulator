
from farm import Factory
from mongoDbDatabase import get_database    


class UsineDAO:

    @staticmethod
    def save_factory(factory: Factory):
        """Ajoute une usine dans MongoDB."""
        db = get_database()
        factory_doc = {
            "input_type": factory.input_type,
            "output_type": factory.output_type,
            "multiplier": factory.multiplier
        }
        db.factories.insert_one(factory_doc)

    @staticmethod
    def load_factories() -> list[Factory]:
        """Charge toutes les usines depuis MongoDB."""
        db = get_database()
        factories = []
        for doc in db.factories.find():
            f = Factory(
                input_type=doc["input_type"],
                output_type=doc["output_type"],
                multiplier=doc["multiplier"]
            )
            factories.append(f)
        return factories
    """def __init__(self, input_type: list[str], output_type: str, multiplier: float):
        self.input_type = input_type
        self.output_type = output_type
        self.multiplier = multiplier

    def __repr__(self):
        return f"Factory(input={self.input_type}, output='{self.output_type}', x{self.multiplier})"""

