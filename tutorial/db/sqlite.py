import sqlite3

""" 连接到一个现有的数据库。如果数据库不存在，那么它就会被创建，最后将返回一个数据库对象 """
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
print('OPEN/CREATE db successfully')


def close_db():
    conn.close()


def create_table():
    """ 创建表 """
    connect_to_db()
    conn.execute('''CREATE TABLE COMPANY
            (ID INT PRIMARY KEY NOT NULL,
            NAME TEXT NOT NULL,
            AGE INT NOT NULL ,
            ADDRESS CHAR(50),
            SALARY REAL);
            ''')
    print('CREATE table successfully')


def insert_table():
    """ INSERT 操作 """
    conn.execute('''INSERT  INTO  COMPANY(ID, NAME, AGE, ADDRESS, SALARY) 
            VALUES (3, 'John', 35, 'Los Angels', 50000) ''')
    conn.commit()
    print('->INSERT table successfully')


def select_table():
    """ SELECT 操作 """
    results = cursor.execute('''SELECT * FROM COMPANY
            ''')
    print_results(results)


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

    # create_table()
    # insert_table()
    select_table()
    update_table()
    select_table()
    delete_table()
    select_table()
    close_db()


if __name__ == '__main__':
    main()
