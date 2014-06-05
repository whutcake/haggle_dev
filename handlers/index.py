import webapp2
import json
from handlers.web.web_request_handler import WebRequestHandler
from google.appengine.api import urlfetch
from platforms_graphs.graph_mappings import view_to_graphmodel_mapping, model_list
from platforms_graphs.util import get_class
from platforms_graphs.model_factory import get_model_objs_for

URL = 'https://haggle-test1.appspot.com/api/analytics/'

class HomepageHandler(WebRequestHandler):
    def get(self):
        path = 'index.html'
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
        url = URL + endpoint + '?token='+token+'&'+data

        response = urlfetch.fetch(url).content
        self.response.out.write(response)

class Landing(WebRequestHandler):
    def get(self):
        path = 'landing.html'
        self.response.out.write(self.get_rendered_html(path, dict()))

class Marketers(WebRequestHandler):
    def get(self):
        path = 'marketers.html'
        self.response.out.write(self.get_rendered_html(path, None))

class MarketersOptions(WebRequestHandler):
    def post(self):
        pass
        '''
        graph_id = self['graph_id']
        graph_view = get_graph_view(graphs[graph_id])
        dimension = graph_view.get_dimension()
        dimension_title = dimension.keys()[0]
        dimensions_html = self.get_rendered_html('marketers/graphs/dimensions_area.html',
                                {'dimension' : dimension_title,
                                 'graph_id' : graph_id})
        filters_html = self.get_rendered_html('marketers/graphs/filters_area.html',
                                              {'filters' : dimension[dimension_title],
                                               'graph_id' : graph_id})
        self.response.headers['Content-Type'] = 'application/json'
        self.write(
            json.dumps(
                {'dimensions':dimensions_html,
                 'filters':filters_html,
                 'graph_id':graph_id
                }))
        '''

class GraphOptions(WebRequestHandler):
    def get(self):
        req_type = self['req_type']
        options = self.get_options_for(req_type)
        self.write(json.dumps(options))

    def get_options_for(self, req_type):
        options = None
        if req_type == 'graph_types':
            options = [graph_type for graph_type in view_to_graphmodel_mapping]
            html = self.get_rendered_html('marketers/graphs/graph_types_area.html', {'types' : options})
        elif req_type == 'models':
            options = [model for model in model_list]
            html = self.get_rendered_html('marketers/graphs/models_area.html', {'types' : options})
        elif req_type == 'dimensions':
            model = model_list[self['model']]
            model_objs = get_model_objs_for(model)
            graph_type = self['graph_type']
            graph_model_name = view_to_graphmodel_mapping[graph_type]
            graph_model_obj = get_class(graph_model_name)()
            name, params = graph_model_obj.get_dimensions_html_for(get_class(model), model_objs)
            html = self.get_rendered_html(name, params)
        return {req_type : html}

app = webapp2.WSGIApplication([('/', HomepageHandler),
                               ('/tutorial', Tutorial),
                               ('/documentation', Documentation),
                               ('/rest_api', RestAPI),
                               ('/iphone_app', AppRedirect),
                               ('/fetch_from_api_server', ServerFetchHandler),
                               ('/contact', Contact),
                               ('/landing', Landing),
                               ('/marketers', Marketers),
                               ('/marketers/options', MarketersOptions),
                               ('/marketers/graph_options',GraphOptions)
])
