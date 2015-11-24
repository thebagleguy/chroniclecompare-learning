import webapp2
import models


class PrefsPage(webapp2.RequestHandler):
    def post(self):
        userprefs = models.get_userprefs()
        try:
            tz_offset = int(self.request.get('tz_offset'))
            userprefs.tz_offset = tz_offset
            userprefs.put()
        except ValueError:
            #not integer
            pass
        
        self.redirect('/')

app = webapp2.WSGIApplication([('/prefs', PrefsPage)], debug=True)