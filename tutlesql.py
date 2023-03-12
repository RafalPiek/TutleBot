import sqlite3

connection =sqlite3.connect('tutlesql.db')
userID=0
def create_table():
    global connection
    try:
        cur=connection.cursor()
        cur.execute("""CREATE TABLE question (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_tekst VARCHAR(255) NOT NULL,
            language VARCHAR(255) NOT NULL""")
    except:
        pass
    try:
        cur=connection.cursor()
        cur.execute("""CREATE TABLE question_users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_tekst VARCHAR(255) NOT NULL,
            language VARCHAR(255) NOT NULL""")
    except:
        pass
def add_task(task,category):#ustawione pod różne interefejsy
    global connection
    global userID
    print("Dodajemy zadanie")
    # task = str(input("Wpisz treść zadania: "))
    # category= str(input("Wpisz kategorie zadania(dom, ogród, praca, inny): "))
    task = str(task)
    category= str(category)
    if task == "0":
        print("Powrót do menu")
    else:
        cur=connection.cursor()
        result=cur.execute("""SELECT COUNT(id_task) FROM task WHERE userID=?""",(userID,)).fetchone()
        id_task=result[0]+1
        cur.execute("""INSERT INTO task(id_task,task,userID,category,status) VALUES (?,?,?,?,'Do zrobienia')""",(id_task,task,userID,category,))
        connection.commit()
        print("Dodano zadanie!")
        
        

def delete_task(task_index):
    global connection
    global userID
    task_index = int(task_index)
    cur =connection.cursor()
    rows_deleted=cur.execute("""Delete from task WHERE id_task=? and userID=?""",(task_index,userID,)).rowcount
    cur.execute(""" UPDATE task set id_task=id_task-1 WHERE userID=? AND id_task >?""",(userID,task_index))
    connection.commit()
    if rows_deleted == 0:
        print("Takie zadanie nie istnieje")
    else:
        print("Usunięto zadanie!")


def login(username,password):
    global connection
    global userID
    cur=connection.cursor()
    while True:
        password=sha256(password.encode('utf-8')).hexdigest()
       
        result=cur.execute("""SELECT id FROM Users WHERE username=? AND password=?""",(username,password,))
        try:
            userID_tuple=result.fetchone()
            userID=userID_tuple[0]
            if userID >= 1: break
            else:
                print("Nieprawidłowy Login lub hasło!")
            if 5==int(input("Ponowić próbę?(Wćsiśnij 5): ")):
                pass
            else:
                return 0
        except:
            print("Nieprawidłowy Login lub hasło!")
            if 5==input("Ponowić próbę?(Wćsiśnij 5): "):
                pass
            else:
                return 0
    print("Zalogowano!")
    return 1

def register(username,password):
    global connection
    cur=connection.cursor()
    while True: 
        if len(password) >= 8:
            password=sha256(password.encode('utf-8')).hexdigest()
            try:
                check_username=cur.execute("""SELECT * FROM Users WHERE username=? """,(username,)).rowcount
                if check_username > 0: print("Nazwa użytkownika już istnieje!")
                else:
                    cur.execute("""INSERT INTO Users(username,password) VALUES (?,?)""",(username,password,))
                    connection.commit()
                    break
            except:
                print("Wystąpił błąd!")
                if 5==input("Ponowić próbę?(Wćsiśnij 5): "):
                    pass
                else:
                    return 0
        else:
            print("Zakrótkie hasło! \n musi zawierać co najmniej 8 znaków!")
    print("Konto zostało zarejestrowane!")
    return 1

def f_modify_task(task_index,modify_task):
    task_index = int(task_index)
    modify_task= int(modify_task)
    if modify_task == 1:
        modify_task="Zrobione"
    elif modify_task==2:
        modify_task="W trakcie"
    else:
        modify_task="Do zrobienia"
    
    cur=connection.cursor()
    cur.execute("""UPDATE task SET status=? WHERE id_task=?""",(modify_task,task_index,))
    connection.commit()
    


def admin_panel():
    global connection
    cur=connection.cursor()
    ##DO TESTOWANIA
    # userID=1
    # username="rafal"
    # password="123456789"
    # password=sha256(password.encode('utf-8')).hexdigest()
    # row=cur.execute("""SELECT id FROM Users WHERE username=? AND password=?""",(username,password,)).fetchone()
    # print(row[0])
    # result=cur.execute("""SELECT COUNT(id_task) FROM task WHERE userID=?""",(userID,)).fetchone()
    # print(result[0])
    # cur.execute("""INSERT INTO task(id_task,task,userID) VALUES (?,?,?)""",(2,"abaaba",userID,))
    # connection.commit()
    # cur.execute("""ALTER TABLE task
    # ADD status VARCHAR(255)""")
    # connection.commit()  