import sqlite3

db_path = "database.db"

def main():
    user_input = "1 OR 1=1"

    init_db()
    print(vulnerable_get_user(user_input))
    print(secure_get_user(user_input))


def init_db():
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
            """
        )

        cursor.execute(
            """
            INSERT OR IGNORE INTO users (username, password) VALUES
            ('admin', 'admin'),
            ('user', 'user')
            """
        )

        conn.commit()


def vulnerable_get_user(user_id: str):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        query = f"SELECT * FROM users WHERE id = {user_id}"

        cursor.execute(query)
        # SELECT * FROM users WHERE id = 1 OR 1=1

        results = cursor.fetchall()
        return results


def secure_get_user(user_id: str):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        query = f"SELECT * FROM users WHERE id = ?"

        cursor.execute(query, (user_id,))
        # SELECT * FROM users WHERE id = '1 OR 1=1'

        results = cursor.fetchall()
        return results

if __name__ == "__main__":
    main()