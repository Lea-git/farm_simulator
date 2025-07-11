from data_access.database import get_connection

class PlayerDAO:

    def create_player(self, name: str, pieces_or: int):
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO player (name, pieces_or) VALUES (%s, %s)"
        cursor.execute(query, (name, pieces_or))
        conn.commit()
        cursor.close()
        conn.close()

    def get_player_by_name(self, name: str):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM player WHERE name = %s"
        cursor.execute(query, (name,))
        player = cursor.fetchone()
        cursor.close()
        conn.close()
        return player