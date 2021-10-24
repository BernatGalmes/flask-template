from api.views import view_hello


def register_routes(app, api):
    @app.route('/hello/<int:identifier>')
    def render_hello(identifier):
        return view_hello(identifier)

