import mysql.connector as a

class DBHelper:
    def __init__(self):
        self.mydb=a.connect(host="localhost",user="root",password="Shree2002@")
        query_1='create database if not exists internship '
        query_2='create table if not exists internship.movies(name varchar(50),actor varchar(50),actress varchar(50),director varchar(50),year_of_release varchar(50))'

        cur=self.mydb.cursor()
        cur.execute(query_1)
        cur.execute(query_2)
        print("created")

    def insert_movies(self,name,actor,actress,director,year_of_release):
        query="insert into internship.movies(name,actor,actress,director,year_of_release) values('{}','{}','{}','{}','{}')".format(name,actor,actress,director,year_of_release)
        print(query)
        cur=self.mydb.cursor()
        cur.execute(query)
        self.mydb.commit()
        print("movie saved to db")

    def fetch_all(self): #fetch all rows from movies table
        query="select * from internship.movies"
        cur=self.mydb.cursor()
        cur.execute(query)
        for row in cur:
            print("name : ",row[0])
            print("actor : ",row[1])
            print("actress : ",row[2])
            print("director : ",row[3])
            print("year_of_release : ",row[4])
            print()
            print()

    def fetch_one(self):   #function which will fetch the rows using actor name
        query="select * from internship.movies where actor = 'Aamir Khan'"
        cur=self.mydb.cursor()
        cur.execute(query)
        for row in cur:
            print("name : ",row[0])
            print("actor : ",row[1])
            print("actress : ",row[2])
            print("director : ",row[3])
            print("year_of_release : ",row[4])
            print()
            print()

        
        

helper=DBHelper()
    #inserting values in movies table
helper.insert_movies("3 Idiots","Aamir Khan","Kareena kapoor","Rajkumar Hirani","2009")
helper.insert_movies("Hera Pheri","Akshay Kumar","Tabu","Priyadarshan","2000")
helper.insert_movies("Conjuring","Patrick Wilson","Vera Farmiga","James Wan","2013")
helper.insert_movies("Lagaan","Aamir Khan","Gracy Singh","Ashutosh Gowariker","2001")

helper.fetch_all()

helper.fetch_one()
