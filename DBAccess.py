#!/usr/bin/env python3
"""
Database acess script. Contains functions for opening a connection
to a database and reading information from it.
USAGE: python3 DBAcess.py <dbname>
"""

import sys
import sqlite3


def open_db(dbname):
    """
    Establishes a connection to the specified DB.
    Args:
        dbname -> string of the DB to connect to
    Returns:
        cursor to the DB
    """
    conn = sqlite3.connect(dbname)

    if conn:
        print("connected to DB")

    cur = conn.cursor()
    return conn, cur


def query_db(sqlString, cur):
    """
    Executes a query on the sql server
    Args:
        sqlString -> the query to execute
        cur -> the cursor to our DB that will execute the query
    Returns:
        list of records
    """
    cur.execute(sqlString)
    recs = cur.fetchall()

    return recs


def close_db(conn, cur):
    """
    Closes a database connect and it's cursor
    Args:
        conn -> database connection
        cur -> cursor to a database
    """
    cur.close()
    conn.close()
    print('Successfully closed DB connection')


def main():
    """
    Main for testing module
    """
    try:
        conn, cur = open_db(sys.argv[1])
    except IndexError:
        print("Invalid arguments")
        print("USAGE: python3 DBAcess.py <dbname>")
        exit(-1)

    sqlString = 'SELECT trans.trans_id, trans.trans_date,  trans.card_num, \
        trans_line.qty, products.prod_desc \
        FROM trans \
        JOIN trans_line, products \
        WHERE trans.trans_id = trans_line.trans_id \
        AND trans_line.prod_num = products.prod_num'

    # sqlString = 'SELECT * FROM products'
    recs = query_db(sqlString, cur)

    for row in recs:
        print(row)

    close_db(conn, cur)

if __name__ == "__main__":
    main()
    exit(0)
