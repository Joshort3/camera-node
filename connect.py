import psycopg2

# Establish a connection to the database by creating a cursor object
# The PostgreSQL server must be accessed through the PostgreSQL APP or Terminal Shell

# conn = psycopg2.connect("dbname=suppliers port=5432 user=postgres password=postgres")

# Or:
def db_connect(masked,maskless):
    conn = psycopg2.connect(host="10.40.0.1", port = 5432, database="pgdb", user="pgadmin", password="csce483team4")

    # Create a cursor object
    cur = conn.cursor()

    # A sample query of all data from the "vendors" table in the "suppliers" database
    cur.execute("""SELECT * FROM images""")
    query_results = cur.fetchall()
    print(query_results)

    # Close the cursor and connection to so the server can allocate
    # bandwidth to other requests
    cur.close()
    conn.close()
#db_connect(1,2)