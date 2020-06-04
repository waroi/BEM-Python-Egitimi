import sqlite3
import subprocess as sp



def create_table():
	conn = sqlite3.connect('db')

	cursor = conn.cursor()

	query = '''
	    CREATE TABLE IF NOT EXISTS todo(
	    	id INTEGER PRIMARY KEY, 
	    	title TEXT, 
	    	description TEXT,
	        status INTEGER
	    )
	'''

	cursor.execute(query)

	conn.commit()
	conn.close()



def add_todo(title,description,status):
	conn = sqlite3.connect('db')

	cursor = conn.cursor()

	query = '''
	    INSERT INTO todo( title,description,status)
	    	        VALUES ( ?,?,? )
	'''

	cursor.execute(query,(title,description,status))

	conn.commit()
	conn.close()



def get_todos():
	conn = sqlite3.connect('db')

	cursor = conn.cursor()

	query = '''
	    SELECT id,title,description
	    FROM todo
	'''

	cursor.execute(query)
	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()

	return all_rows

def get_todo_by_id(id):
	conn = sqlite3.connect('db')
	cursor = conn.cursor()
	query = '''
		select title,description,status
		from todo
		where id = {}'''.format(id)
	cursor.execute(query)
	all_rows = cursor.fetchone()

	conn.commit()
	conn.close()

	return all_rows


def get_todo_by_roll(title):
	conn = sqlite3.connect('db')

	cursor = conn.cursor()

	query = '''
	    SELECT title,description,status
	    FROM todo
	    WHERE status = {}
	''' .format(title)

	cursor.execute(query)
	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()

	return all_rows

def update_todo(title,description,status,id):
	conn = sqlite3.connect('db')

	cursor = conn.cursor()
	if title == "" and description != "":
		query = '''
		    UPDATE todo
		    SET description = '{}', status = {}
		    WHERE id = {}
		'''.format(description,status, id)
	elif title == "" and description == "" :
		query = '''
		    UPDATE todo
		    SET  status = {}
		    WHERE id = {}
		'''.format(status, id)
	elif title != "" and description == "":
		query = '''
		    UPDATE todo
		    SET title = '{}', status = {}
		    WHERE id = {}
		'''.format(title,status, id)
	elif title != "" and description != "":
		query = '''
		    UPDATE todo
		    SET title = '{}', description = '{}', status = {}
		    WHERE id = {}
		'''.format(title,description,status, id)

	cursor.execute(query)

	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()
	print (all_rows)


def show_data_by_status(id_):
	todo = get_todo_by_roll(id_)
	if not todo:
		print("Bu durumda todo bulunamadı",id_)
	else:
		cursor.execute(query,(title,description,status))

		conn.commit()
		conn.close()


def delete_todo(id):
	conn = sqlite3.connect('db')

	cursor = conn.cursor()

	query = '''
	    DELETE
	    FROM todo
	    WHERE id = {}
	''' .format(id)

	cursor.execute(query)
	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()

	return all_rows



create_table()




def add_data(title,description,status):
	add_todo(title,description,status)
def get_data():
	return get_todos()

def show_data():
	todos = get_data()
	head = ["Id","Başlık","Açıklama"]
	row_format ="|{:>5}" + ("|{:>30}" * (len(head) - 1))
	print(row_format.format(*head))
	for row in todos:
		print("-"*120)
		print(row_format.format(*row))

def show_data_by_status(id_):
	todos = get_todo_by_roll(id_)
	if not todos:
		print("Bu durumda todo bulunamadı",id_)
	else:
		print (todos)

def show_data_by_id(id__):
	todos = get_todo_by_id(id__)
	if not todos:
		print("Bu durumda todo bulunamadı", id__)
	else:
		print(todos)
def show_data_by_status(id_):
	todos = get_todo_by_roll(id_)
	if not todos:
		print("No data found at status",id_)
	else:
		print (todos)

def manage():
	sp.call('cls',shell=True)
	sel = input("1.Todo Ekle\n2.Listemi Göster\n3.ID'ye Göre Ara\n4.Güncelle\n5.Sil\n6.Çıkış\n\n")

	
	if sel=='1':
		sp.call('cls',shell=True)
		id_ = str(input('Başlık: '))
		name = str(input('Açıklama: '))
		phone = str(input('Durum (0-1): '))
		add_data(id_,name,phone)
	elif sel=='2':
		sp.call('cls',shell=True)
		show_data()
		input("\n\nGeri Dönmek için (Enter):")
	elif sel=='3':
		sp.call('cls',shell=True)
		id__ = int(input('Durum Gir (0-1): '))
		show_data_by_status(id__)
		input("\n\nGeri Dönmek için (Enter):")
	elif sel=='4':
		sp.call('cls',shell=True)
		id__ = int(input('Id Gir: '))
		show_data_by_id(id__)
		print()
		title = str(input('Başlık: '))
		descrip = str(input('Açıklama: '))
		status = int(input('Durum: '))
		update_todo(title,descrip,status,id__)
		input("\n\nTodo Güncellendi \nGeri Dönmek için (Enter):")
	elif sel=='5':
		sp.call('cls',shell=True)
		id__ = int(input('Id Gir: '))
		show_data_by_id(id__)
		delete_todo(id__)
		input("\n\nTodo Silindi \nGeri Dönmek için (Enter):")
	else:
		return 0;
	return 1;

while(manage()):
	pass