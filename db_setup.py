from setup_utils import get_random_number, first_name, last_name


def setup_database(connection):
    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'customer');"
        )
        table_exists = cursor.fetchone()[0]

        if not table_exists:
            cursor.execute(
                """
                        CREATE TABLE IF NOT EXISTS customer (
                            id SERIAL PRIMARY KEY,
                            firstname VARCHAR(255),
                            lastname VARCHAR(255),
                            age INT
                        );
                    """
            )
            for i in range(20):
                fname = get_random_number(19)
                firstname = first_name[fname]
                lname = get_random_number(19)
                lastname = last_name[lname]
                age = get_random_number(100)
                cursor.execute(
                    "INSERT INTO customer (firstname, lastname, age) VALUES (%s, %s, %s);",
                    (firstname, lastname, age),
                )

        connection.commit()
        cursor.close()
        connection.close()

    except Exception as e:
        print(f"An error occurred: {e}")
        if connection:
            connection.rollback()
