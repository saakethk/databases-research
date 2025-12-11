from dbmodule import connect 

# Creates connection
Connection = connect("databasename", "username", "pswd")

# Created cursor object
Cursor = Connection.cursor()

# Run queries with
Cursor.execute("select * from table")
Results = Cursor.fetchall()

# Free up resources
Cursor.close() # <- Very Important