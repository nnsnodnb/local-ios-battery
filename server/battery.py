from bottle import default_app, run, route, request, response, template
from database import Database


@route('/', method='GET')
def index():
    return template('index')


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

    db.battery_insert(request.json)

    return 'Success'


@route('/token', method='PUT')
def receive_device_token():
    """
    Sample request
    $ curl -X PUT http://HOSTNAME/token -H 'Content-Type: application/json' \
           -d '{"token":"XXXXXXXXXXXXXX", "uuid": "XXXXXXX"}'
    """
    if 'token' not in request.json:
        return response(body='Required "Device Token"', status=401)
    if 'uuid' not in request.json:
        return response(body='Required "UUID"', status=401)

    if db.is_token(request.json['uuid']):
        db.token_update(request.json)
    else:
        db.token_insert(request.json)

    return 'Success'


app = default_app()
db = Database()


if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True, reloader=True)
