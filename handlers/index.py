import webapp2
from django.template import loader

from google.appengine.api import urlfetch

URL = 'https://haggle-test1.appspot.com/api/analytics/'

class WebRequestHandler(webapp2.RequestHandler):
    def render_template(self, template_name, template_values = None):
        self.response.out.write(self.get_rendered_html(template_name, template_values))

    def get_rendered_html(self, template_name, template_values = None):
        return loader.render_to_string(template_name, template_values)

class HomepageHandler(WebRequestHandler):
    def get(self):
        path = 'index.html'
        self.response.out.write(self.get_rendered_html(path, dict()))

class Overview(WebRequestHandler):
    def get(self):
        path = 'integrate_code.html'
        self.response.out.write(self.get_rendered_html(path, dict()))

class Tutorial(WebRequestHandler):
    def get(self):
        path = 'tutorial.html'
        self.response.out.write(self.get_rendered_html(path, dict()))

class RestAPI(WebRequestHandler):
    def get(self):
        path = 'rest_api.html'
        self.response.out.write(self.get_rendered_html(path, dict()))

class AppRedirect(WebRequestHandler):
    def get(self):
        path = 'iphone_app.html'
        self.response.out.write(self.get_rendered_html(path, dict()))

class Contact(WebRequestHandler):
    def get(self):
        path = 'contact.html'
        self.response.out.write(self.get_rendered_html(path, dict()))

class Documentation(WebRequestHandler):
    def get(self):
        path = 'integrate_docs.html'
        self.response.out.write(self.get_rendered_html(path, dict()))

class ServerFetchHandler(webapp2.RequestHandler):
    def post(self):
        data = self.request.get('data')
        endpoint = self.request.get('endpoint')
        token = self.request.get('token')
        url = URL + endpoint + '?' + data
        response = urlfetch.fetch(url).content
        self.response.out.write(response)

class CaseStudies(WebRequestHandler):
    def get(self):
        path = 'integrate_case-studies.html'
        self.response.out.write(self.get_rendered_html(path, dict()))

class Landing(WebRequestHandler):
    def get(self):
        path = 'landing.html'
        self.response.out.write(self.get_rendered_html(path, dict()))

app = webapp2.WSGIApplication([('/', HomepageHandler),
                               ('/overview', Overview),
                               ('/tutorial', Tutorial),
                               ('/documentation', Documentation),
                               ('/rest_api', RestAPI),
                               ('/iphone_app', AppRedirect),
                               ('/fetch_from_api_server', ServerFetchHandler),
                               ('/contact', Contact),
                               ('/case_studies', CaseStudies),
                               ('/landing', Landing)
])
