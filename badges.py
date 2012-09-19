import webapp2

class MainPage(webapp2.RequestHandler):
  def get(self):
      self.response.headers['Content-Type'] = 'html'
      self.response.write('''
            <html>
            <body>
                <marquee><blink>Hello, webapp2 World!!!!</blink></marquee>
            </body>
            </html>
            ''')

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)
