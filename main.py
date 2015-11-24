import webapp2
import os
import jinja2
import datetime
import models
from google.appengine.ext import db
from google.appengine.api import users


template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))


class MainHandler(webapp2.RequestHandler):
 def get(self):
  current_time = datetime.datetime.now()
  user = users.get_current_user()
  login_url = users.create_login_url(self.request.path)
  logout_url = users.create_logout_url(self.request.path)
  userprefs = models.get_userprefs()
  
  if userprefs:
   current_time += datetime.timedelta( 0, 0, 0, 0, 0, userprefs.tz_offset)
  
  template = template_env.get_template('main.html')
  context = {
   'current_time': current_time,
   'user': user,
   'login_url': login_url,
   'logout_url': logout_url,
   'userprefs': userprefs,
  }
  self.response.out.write(template.render(context))

 
 
 
 
app = webapp2.WSGIApplication([('/', MainHandler)], debug=True)