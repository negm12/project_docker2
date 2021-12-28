star = """
a >>>>>> add skill
d >>>>>> delete skill
u >>>>>> update skill
s >>>>>> show skill
all >>> show all skills
""".capitalize()
import sqlite3
db = sqlite3.connect("sklills.db")
cr = db.cursor()
cr.execute("create table if not exists skill (name text , progress integer , id integer)")
def start():
    print(star)
    choce = input("select what do you want to do : ")
    if choce == 'a':
        add()
    elif choce == 'd':
        delete()
    elif choce == 'u':
        update()
    elif choce == 's':
        show()
    elif choce == "all":
        show_all()


def commit_and_close():
    flage = input("do you want to contenue 'y' or 'n' ").lower()
    if flage == 'y':
        start()
    else:
        db.commit()
        db.close()
        print("data base closed successfully".capitalize())


def add():
    name = input("enter the skill name : ").strip().capitalize()
    prog = input("enter the skill progress : ").strip()
    id = input("enter the student id : ").strip()
    cr.execute(f"select name from skill where id = '{id}' and name = '{name}'" )
    result = cr.fetchall()
    #print(result)

    if len(result) == 0:
        cr.execute(f"insert into skill (name , progress , id) values ('{name}' , '{prog}' , '{id}' )")

    else:
        print("this skill allredy exist you cant add it :  ")
        print("do you want to update it 'y' or 'n' ")
        choce2 = input("press 'y' if you want to update : ")

        if choce2 == 'y':
            cr.execute(f"update skill set progress = '{prog}' where name = '{name}' and id = '{id}'")
            print("the data updated successfully .")

    commit_and_close()

def delete():
    name = input("enter the skill name : ").strip().capitalize()
    id = input("enter the student id : ").strip()
    cr.execute(f"delete from skill where name = '{name}' and id = '{id}' ")
    commit_and_close()

def update():
    name = input("enter the skill name : ").strip().capitalize()
    prog = input("enter the skill progress : ").strip()
    id = input("enter the student id : ").strip()
    cr.execute(f"update skill set progress = '{prog}' where name = '{name}' and id = '{id}'")
    commit_and_close()

def show():
    name = input("enter the skill name : ").strip().capitalize()
    id = input("enter the student id : ").strip()
    cr.execute(f"select * from skill where name = '{name}' and id = '{id}'")
    print(cr.fetchall())

def show_all():
    cr.execute(f"select * from skill ")
    value = cr.fetchall()
    for v in value:
        print(f"the skill name is : {v[0]} and the skill progress {v[1]}% "
              f"and student id is {v[2]} ")
    commit_and_close()

start()