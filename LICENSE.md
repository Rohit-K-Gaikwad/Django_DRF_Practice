ROHIT-GAIKWAD License

Copyright (c) 2023 Rohit_Gaikwad

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.







import mysql.connector
from mysql.connector import Error
from typing import Optional

def connect_to_mysql(host: str, username: str, password: str, database: str, port: Optional[int] = 3306):
    """
    Connect to MySQL database.

    Args:
        host (str): The hostname or IP address of the MySQL server.
        username (str): The username for accessing the MySQL server.
        password (str): The password for accessing the MySQL server.
        database (str): The name of the database to connect to.
        port (int, optional): The port number of the MySQL server. Defaults to 3306.

    Returns:
        Connection: MySQL connection object if successful, None otherwise.
    """
    try:
        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database,
            port=port
        )
        print("Connected to MySQL Server")
        return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

def close_connection(connection):
    """
    Close the connection to the MySQL database.

    Args:
        connection: MySQL connection object to close.
    """
    if connection:
        connection.close()
        print("MySQL connection closed")

# Example usage:
if __name__ == "__main__":
    host = "localhost"
    username = "your_username"
    password = "your_password"
    database = "your_database_name"
    port = 3306

    connection = connect_to_mysql(host, username, password, database, port)
    if connection:
        # Perform database operations here
        close_connection(connection)