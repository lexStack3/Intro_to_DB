#!/usr/bin/env python
"""Creates a database <alx_book_store> if it doesn't exist."""
import mysql.connector
import os

def main():
    """Creates a database if it doesn't exist."""

    conn, cursor = None, None

    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            passwd=os.getenv("DB_PASSWD")
            );
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
    except Exception as err:
        print(f"{err.__class__.__name__}: {err}")
    else:
        print("Database 'alx_book_store' created successfully!")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
