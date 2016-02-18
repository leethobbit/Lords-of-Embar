from webapp2 import RequestHandler, cached_property
from webapp2_extras import json, jinja2


class BaseRequestHandler(RequestHandler):
    @cached_property
    def jinja2(self):
        jinja2.default_config.update(
            template_path=self.app.config.get('template_path', 'templates')
        )
        return jinja2.get_jinja2(app=self.app)

    def json_view(self, content=None, **kwds):
        content = content or kwds
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(json.encode(content))

    def html_view(self, template, context=None, **kwds):
        content = self.jinja2.render_template(template, **(context or kwds))
        self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
        self.response.write(content)
