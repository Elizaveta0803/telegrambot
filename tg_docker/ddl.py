from clickhouse_driver import Client


def db_connect():
    connection = Client(
        host="ch_db",
        user="default",
        password="",
        port=9000,
    )

    try:
        connection.execute("CREATE DATABASE todo")
        connection.execute("""CREATE TABLE todo.todo (
		    id UUID,
		    text String,
		    status String
		) engine = MergeTree() order by id""")
    except:
        pass
