from bottle import default_app, run, route, request, response
from database import Database


@route('/receive', method='POST')
def receive_battery():
    """
    Sample request
    $ curl -X POST http://HOSTNAME/receive -H 'Content-Type: application/json' \
           -d '{"name":"iPhone SE", "battery":"99.0", "uuid":"XXXXXXX"}'
    """
    if 'name' not in request.json:
        return response(body='Required "Name of Device"', status=401)
    if 'battery' not in request.json:
        return response(body='Required "Battery Status"', status=401)
    if 'uuid' not in request.json:
        return response(body='Required "UUID"', status=401)

    Database().insert(request.json)

    return response(body='Success', status=200)


app = default_app()
Database()

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True, reloader=True)
