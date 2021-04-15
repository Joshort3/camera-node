import psycopg2
import datetime

# Establish a connection to the database by creating a cursor object
# The PostgreSQL server must be accessed through the PostgreSQL APP or Terminal Shell

# conn = psycopg2.connect("dbname=suppliers port=5432 user=postgres password=postgres")

# Or:
def db_connect(masked,maskless):
    conn = psycopg2.connect(host="10.40.0.1", port = 5432, database="pgdb", user="pgadmin", password="csce483team4")
    # Create a cursor object
    day = datetime.datetime.now().strftime("%A")
    hour = datetime.datetime.now().hour
    cur = conn.cursor()
    SQL_command = "SELECT * FROM without_facemasks WHERE day = '" + day + "';"
    # A sample query of all data from the "vendors" table in the "suppliers" database
    cur.execute("""SELECT column_name FROM information_schema.columns WHERE table_name ='without_facemasks';""")
    query_results1 = cur.fetchall()
    print(query_results1)
    cur.execute(SQL_command)
    query_results2 = cur.fetchall()
    prev_maskless = query_results2[0][hour+1]
    maskless = maskless + prev_maskless
    print(query_results2)
    print(maskless)
    print(hour)
    SQL_command = "UPDATE without_facemasks SET hour" + str(hour) + " = " + str(maskless) + " WHERE day = '" + day + "' RETURNING *;"
    cur.execute(SQL_command)
    query_results3 = cur.fetchall()
    print(query_results3)
    print (SQL_command)

    # Close the cursor and connection to so the server can allocate
    # bandwidth to other requests
    cur.close()
    conn.close()
db_connect(1,2)