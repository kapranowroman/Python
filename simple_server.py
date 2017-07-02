# coding: utf-8
import cgi
import json
from urllib.parse import parse_qs


def app(environ, start_response):
    if environ['PATH_INFO'] == '/magnit':
        status = '200 OK'
        response_headers = [('Content-type', 'text/html')]
        start_response(status, response_headers)
        
        qstr= environ['QUERY_STRING']

        test = b'<H1>'+str.encode(qstr)+b'</H1>'
        params = parse_qs(environ['QUERY_STRING'])
        print (params.get('command',[]))
        if params.get('command',['',''])[0]=='START':
            print('YES')
            test = b'<h1>'+str.encode(params['command'][0])+b'</h1>'
        print (params)
        return [test]


if __name__ == '__main__':
    try:
        from wsgiref.simple_server import make_server
        httpd = make_server('', 8088, app)
        print('Serving on port 8088...')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Goodbye.')
