import psycopg2
import datetime

# Establish a connection to the database by creating a cursor object
# The PostgreSQL server must be accessed through the PostgreSQL APP or Terminal Shell

# conn = psycopg2.connect("dbname=suppliers port=5432 user=postgres password=postgres")

# Or:
def db_connect(masked,maskless):
    conn = psycopg2.connect(host="10.40.0.1", port = 5432, database="pgdb", user="pgadmin", password="csce483team4")
    
    # Create a cursor object and current time data
    
    day = datetime.datetime.now().strftime("%A")
    hour = datetime.datetime.now().hour
    cur = conn.cursor()
    
    #SQL Commands to grab current numbers
    SQL_command_maskless = "SELECT * FROM without_facemasks WHERE day = '" + day + "';"
    SQL_command_masked = "SELECT * FROM with_facemasks WHERE day = '" + day + "';"


    # Update wtihout_facemasks table
    cur.execute(SQL_command_maskless)
    query_results_maskless = cur.fetchall()
    prev_maskless = query_results_maskless[0][hour+1]
    maskless = maskless + prev_maskless
    SQL_command_maskless = "UPDATE without_facemasks SET hour" + str(hour) + " = " + str(maskless) + " WHERE day = '" + day + "' RETURNING *;"
    cur.execute(SQL_command_maskless)
    
    # Update wtih_facemasks table
    cur.execute(SQL_command_masked)
    SQL_command_masked = cur.fetchall()
    prev_masked = SQL_command_masked[0][hour+1]
    masked = masked + prev_masked
    SQL_command_masked = "UPDATE with_facemasks SET hour" + str(hour) + " = " + str(maskless) + " WHERE day = '" + day + "' RETURNING *;"
    cur.execute(SQL_command_masked)
    
    
    conn.commit()
    query_results3 = cur.fetchall()

    # Close the cursor and connection to so the server can allocate
    # bandwidth to other requests
    cur.close()
    conn.close()
    print("Database Connection Finished!!!")
#db_connect(1,2)