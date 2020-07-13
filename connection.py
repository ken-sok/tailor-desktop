import psycopg2
from psycopg2 import Error

#credentials

PGHOST='127.0.0.1'
PGPORT = '5432'
PGDATABASE='tailor_store'
PGUSER='tailor_owner'
PGPASSWORD='tailor'

try:

    connection = psycopg2.connect(user=PGUSER,
                                  password=PGPASSWORD,
                                  host=PGHOST,
                                  port=PGPORT,
                                  database=PGDATABASE)

    # create a cursor object which allows us to execute PostgreSQL command through Python source code.
    cursor = connection.cursor()

    # Print PostgreSQL Connection properties
    #print(connection.get_dsn_parameters(), "\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)


def close_connection(connection, cursor): 
    '''this function closes the connection instance with postgre''' 
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
    else: 
        print("connection not found")

#close_connection(connection, cursor)
