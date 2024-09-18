from database import get_db_cursor


def initialize_database():
    with get_db_cursor() as cursor:

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                link VARCHAR(255) NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS book_logs (
                id SERIAL PRIMARY KEY,
                price INTEGER NOT NULL,
                date DATE NOT NULL,
                       
                book_id INTEGER NOT NULL,
                FOREIGN KEY (book_id) REFERENCES books(id),
                       
                CONSTRAINT unique_book_log UNIQUE (date, book_id)
            )
        """)


if __name__ == "__main__":
    initialize_database()
    print("Banco de dados inicializado com sucesso.")
