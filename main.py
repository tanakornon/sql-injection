import sqlite3

def main():
    user_input = "1 OR 1=1"

    vulnerable_get_user(user_input)
    secure_get_user(user_input)


def vulnerable_get_user(user_id: str):
    with sqlite3.connect('example.db') as conn:
        cursor = conn.cursor()

        query = f"SELECT * FROM users WHERE id = {user_id}"

        cursor.execute(query)
        # SELECT * FROM users WHERE id = 1 OR 1=1

        results = cursor.fetchall()
        return results


def secure_get_user(user_id: str):
    with sqlite3.connect('example.db') as conn:
        cursor = conn.cursor()

        query = f"SELECT * FROM users WHERE id = ?"

        cursor.execute(query, (user_id,))
        # SELECT * FROM users WHERE id = '1 OR 1=1'

        results = cursor.fetchall()
        return results

if __name__ == "__main__":
    main()