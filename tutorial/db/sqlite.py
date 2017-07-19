import sqlite3

import sys

""" 连接到一个现有的数据库。如果数据库不存在，那么它就会被创建，最后将返回一个数据库对象 """
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
print('OPEN/CREATE db successfully')


def close_db():
    cursor.close()
    conn.close()


def create_table():
    """ 创建表 """
    cursor.execute('''CREATE TABLE COMPANY
            (ID INT PRIMARY KEY NOT NULL,
            NAME TEXT NOT NULL,
            AGE INT NOT NULL ,
            ADDRESS CHAR(50),
            SALARY REAL);
            ''')
    print('CREATE table successfully')


def insert_table():
    """ INSERT 操作 """
    cursor.execute('''INSERT  INTO  COMPANY(ID, NAME, AGE, ADDRESS, SALARY) 
            VALUES (3, 'John', 35, 'Washington', 50000) ''')
    conn.commit()
    print('->INSERT %d rows' % cursor.rowcount)


def select_table():
    """ SELECT 操作 """
    cursor.execute('''SELECT * FROM COMPANY
            ''')
    print_results(cursor.fetchall())  # 通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录


def update_table():
    """ UPDATE 操作 """
    cursor.execute('''UPDATE COMPANY SET SALARY=30000 WHERE ID=1
            ''')
    conn.commit()
    print("->UPDATE changes: " + str(conn.total_changes))


def delete_table():
    """ DELETE 操作 """
    cursor.execute('''DELETE FROM COMPANY WHERE ID=3
            ''')
    conn.commit()
    print("->DELETE changes: " + str(conn.total_changes))


def print_results(results):
    for result in results:
        print("ID: " + str(result[0]))
        print("NAME: " + result[1])
        print("AGE: " + str(result[2]))
        print("ADDRESS: " + result[3])
        print("SALARY: " + str(result[4]) + '\n')


def main():
    print("module sqlite3: ")
    print(dir(sqlite3))

    try:
        # create_table()
        insert_table()
        select_table()
        update_table()
        select_table()
        delete_table()
        select_table()
    except:
        print('Unexpected Error: ' + str(sys.exc_info()))
    finally:
        close_db()


if __name__ == '__main__':
    main()
