import pyodbc

def get_connection():
    SERVER = '<server-address>'
    DATABASE = 'Desarrollo'
    USERNAME = '<username>'
    PASSWORD = '<password>'
    connectionString = f"""
        DRIVER={{ODBC Driver 18 for SQL Server}};
        SERVER={SERVER};
        DATABASE={DATABASE};
        UID={USERNAME};
        PWD={PASSWORD}"""

    conn = pyodbc.connect(connectionString)
    return conn