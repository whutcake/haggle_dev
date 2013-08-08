import webapp2
import logging
from django.template import loader

class WebRequestHandler(webapp2.RequestHandler):
    def render_template(self, template_name, template_values = None):
        self.response.out.write(self.get_rendered_html(template_name, template_values))
        
    def get_rendered_html(self, template_name, template_values = None):
        return loader.render_to_string(template_name, template_values)

class DevelopersHomepageHandler(WebRequestHandler):
    def get(self):
    	path = 'home.html'
        self.response.out.write(self.get_rendered_html(path, dict()))

class DevelopersOverview(WebRequestHandler):
	def get(self):
		path = 'overview.html'
		self.response.out.write(self.get_rendered_html(path, dict()))

class DevelopersDocumentation(WebRequestHandler):
	def get(self):
		path = 'documentation.html'
		self.response.out.write(self.get_rendered_html(path, dict()))

class DevelopersTutorial(WebRequestHandler):
	def get(self):
		path = 'tutorial.html'
		self.response.out.write(self.get_rendered_html(path, dict()))

class DevelopersRestAPI(WebRequestHandler):
	def get(self):
		path = 'rest_api.html'
		self.response.out.write(self.get_rendered_html(path, dict()))

class DevelopersSDK(WebRequestHandler):
	def get(self):
		path = 'sdk_iphone.html'
		self.response.out.write(self.get_rendered_html(path, dict()))

class DevelopersSDKAndroid(WebRequestHandler):
	def get(self):
		path = 'sdk_android.html'
		self.response.out.write(self.get_rendered_html(path, dict()))

class DevelopersAppRedirect(WebRequestHandler):
	def get(self):
		path = 'iphone_app.html'
		self.response.out.write(self.get_rendered_html(path, dict()))

class DevelopersEndpoints(WebRequestHandler):
	def get(self):
		path = 'endpoints.html'
		self.response.out.write(self.get_rendered_html(path, dict()))


app = webapp2.WSGIApplication([('/', DevelopersHomepageHandler),
	('/overview', DevelopersOverview),
	('/documentation', DevelopersDocumentation),
	('/tutorial', DevelopersTutorial),
	('/rest_api', DevelopersRestAPI),
	('/sdk_iphone', DevelopersSDK),
	('/sdk_android', DevelopersSDKAndroid),
	('/iphone_app', DevelopersAppRedirect),
	('/endpoints', DevelopersEndpoints)
	])
