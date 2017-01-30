import endpoints
from endpoints import Controller
import sqlite3
import json

class Default(Controller):
    def GET(self):
       return 

    def POST(self, **kwargs):
        return

class Posts(Controller):
    def GET(self):
        conn = sqlite3.connect('blog.db')
        c = conn.cursor()
        for row in c.execute('SELECT * FROM posts'):
            print row 
        conn.close()

class Post(Controller):
   def POST(self, **kwargs):
        row = (kwargs['post_id'] , kwargs['title'], kwargs['body'])
        conn = sqlite3.connect('blog.db')
        c = conn.cursor()
        try:
           c.execute('INSERT INTO posts (post_id,title,body) VALUES(?,?,?)', row ) 
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
        conn.commit()
        conn.close()
        return 'Posted blog id {}'.format(kwargs['post_id'])
    

