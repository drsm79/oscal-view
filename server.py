import argparse
import http
import webbrowser
import json

from collections import namedtuple
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs


schemas = {
    'catalog': 'OSCAL/json/schema/oscal_catalog_schema.json',
    'profile': 'OSCAL/json/schema/oscal_profile_schema.json',
    'component': 'OSCAL/json/schema/oscal_component_schema.json',
    'ssp': 'OSCAL/json/schema/oscal_ssp_schema.json'
}

to_replace = '''{
    	"title": "Example Schema",
    	"type": "object",
    	"properties": {
    		"firstName": {
    			"type": "string"
    		},
    		"lastName": {
    			"type": "string"
    		},
    		"age": {
    			"description": "Age in years",
    			"type": "integer",
    			"minimum": 0
    		}
    	},
    	"required": ["firstName", "lastName"]
    }'''

def populate_schemas():
    for k, v in schemas.items():
        with open(v) as f:
            schemas[k] = f.read()

def statics(parts):
    with open(f'jsonschemaviewer/{parts[0]}/{parts[1]}') as f:
        return f.read()

def inject_schema(parts, template_string):
    # show_me = 'catalog'
    if parts[0] in schemas:
        show_me = parts[0]
        return template_string.replace(to_replace, schemas[show_me])

    return template_string


class SchemaHandler(BaseHTTPRequestHandler):
    template_string = None

    def do_GET(self):
        request = urlparse(self.path)
        parts = request.path.strip('/').rsplit('/')
        if parts[0] == 'css':
            self.send_content('text/css',statics(parts))
        elif parts[0] == 'js':
            self.send_content('text/javascript;charset=UTF-8',statics(parts))
        else:
            self.send_content('text/html', self.render_page(parts))

    def render_page(self, parts):
        if not self.template_string:
            with open('jsonschemaviewer/index.html') as f:
                template_string = f.read()
        return inject_schema(parts, template_string)

    def send_content(self, ctype, value):
        self.send_response(200)
        self.send_header('Content-type',ctype)
        self.end_headers()
        self.wfile.write(value.encode('utf-8'))


def run():
    populate_schemas()
    port = 8000
    server_address = ('', port)
    httpd = HTTPServer(server_address, SchemaHandler)
    webbrowser.open_new_tab(f'http://localhost:{port}/')
    httpd.serve_forever()


if __name__ == "__main__":
    run()