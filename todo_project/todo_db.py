import click
import MySQLdb
from datetime import date
import random
from todo_project import wsgi
from todo_app.models import *

def get_random_date():
    start_date = date.today().replace(day=1, month=1).toordinal()
    end_date = date.today().toordinal()
    random_day = date.fromordinal(random.randint(start_date, end_date))
    return random_day

@click.group()
def dbcommands():
    pass

@dbcommands.command()
@click.argument('user')
@click.argument('passwd')
@click.argument('dbname')
def createdb(user, passwd, dbname):
    db = MySQLdb.connect(user=user, passwd=passwd, host='localhost', port=3306)
    cur = db.cursor()
    try:
        cur.execute("CREATE DATABASE " + dbname)
    except Exception as e:
        print e
    finally:
        db.close()

@dbcommands.command()
@click.argument('user')
@click.argument('passwd')
@click.argument('dbname')
def dropdb(user, passwd, dbname):
    db = MySQLdb.connect(user=user, passwd=passwd, host='localhost', port=3306)
    cur = db.cursor()
    try:
        cur.execute("DROP DATABASE " + dbname)
    except Exception as e:
        print e
    finally:
        db.close()


@dbcommands.command()
def populate():
    for list_number in xrange(1, 6):
        list_name=raw_input('enter list item')
        list = to_do_list(name=list_name, create_date=date.today())
        list.save()
        for list_item_number in xrange(1, 6):
            list_item_name = raw_input('enter data item')
            due_date = get_random_date()
            if (random.randrange(0, 2)):
                completed = True
            else:
                completed = False
            list_item = to_do_item(description=list_item_name, due_date=due_date, completed=completed, list=list)
            list_item.save()

@dbcommands.command()
def drop():

    to_do_list.objects.all().delete()
    to_do_item.objects.all().delete()


if __name__ == "__main__":
    dbcommands()