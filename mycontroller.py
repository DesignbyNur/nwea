import endpoints
from endpoints import Controller

class Default(Controller):
    def GET(self):
       return 

    def POST(self, **kwargs):
        return

class Posts(Controller):
    def GET(self):
        return "/posts GET"

class Post(Controller):
   def POST(self, **kwargs):
        return 'hello Post {}'.format(kwargs['name'])

