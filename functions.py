def connect_to_AWS():
    cnx = mysql.connector.connect(
        host = config.host,
        user = config.user,
        passwd = config.password
    )
    return cnx

def close_connections():
    cursor.close()
    conn.close()