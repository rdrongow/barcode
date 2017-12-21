from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import FileResponse
from pyramid.view import view_config
import my_barcode


@view_config(
    route_name='barcode',
    renderer='templates/barcode.jinja2')
def barcode(request):
    return []


@view_config(
    route_name='barcode',
    request_method='POST')
def post(request):
    nr_eans = my_barcode.upload_to_tuple(request.POST['file'].file)
    eans = my_barcode.create_eans(nr_eans)
    myzip = my_barcode.create_zipfile(eans)
    return FileResponse(myzip, content_type='application/zip')


if __name__ == '__main__':
    with Configurator() as config:
        config.include('pyramid_jinja2')
        config.add_route('barcode', '/')
        config.scan()
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
