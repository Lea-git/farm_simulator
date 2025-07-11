from datetime import date as Date

class PricingDao:
    def __init__(self, db_connection):
        self.connection = db_connection

    def get_base_price(self, pass_type):
        cursor = self.connection.cursor()
        query = "SELECT cost FROM base_price WHERE type = ?"
        cursor.execute(query, (pass_type,))
        row = cursor.fetchone()
        cursor.close()

        if row:
            return row[0]
        else:
            raise ValueError(f"No base price found for type '{pass_type}'")

    def is_holiday(self, date_obj: Date) -> bool:
        cursor = self.connection.cursor()
        query = "SELECT holiday FROM holidays"
        cursor.execute(query)
        holidays = cursor.fetchall()
        cursor.close()

        for (holiday,) in holidays:
            if (
                holiday.year == date_obj.year and
                holiday.month == date_obj.month and
                holiday.day == date_obj.day
            ):
                return True
        return False

    def save_booking(self, pass_info):
        # Tu peux créer une table 'bookings' si tu veux vraiment stocker
        # ce n’est pas requis dans l’énoncé, donc on peut laisser vide ou loguer
        print(f"Booking saved: {pass_info}")