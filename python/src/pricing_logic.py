from datetime import datetime
import math

class PricingLogic:
    def __init__(self, dao):
        self.dao = dao

    def calculate_price(self, pass_info):
        pass_type = pass_info.get("type")
        age = pass_info.get("age", None)
        date_str = pass_info.get("date", None)

        base_cost = self.dao.get_base_price(pass_type)
        cost = base_cost

        if age is not None and age < 6:
            return 0

        # Réduction par défaut pour le type "night"
        if pass_type == "night":
            if age is None:
                return cost
            elif age > 64:
                return math.ceil(cost * 0.4)
            else:
                return cost

        # Vérification des jours fériés
        is_holiday = False
        reduction = 0
        if date_str:
            try:
                date_obj = datetime.fromisoformat(date_str)
            except ValueError:
                raise ValueError("Invalid date format, expected YYYY-MM-DD")

            if self.dao.is_holiday(date_obj):
                is_holiday = True
            elif date_obj.weekday() == 0:  # Lundi
                reduction = 35

        # Réductions par âge
        if age is not None and age < 15:
            cost = cost * 0.7
        elif age is not None and age > 64:
            cost = cost * 0.75 * (1 - reduction / 100)
        else:
            cost = cost * (1 - reduction / 100)

        return math.ceil(cost)

    def calculate_multiple_prices(self, passes):
        return [{"cost": self.calculate_price(p)} for p in passes]

    def confirm_booking(self, passes):
        for p in passes:
            self.dao.save_booking(p)