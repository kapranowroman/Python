# coding: utf-8
import cgi
import sys
import os
import json


from commentForm import form
from db_magnit import messdelfrombase, regstat, citystat
from messtat import messstat
from messviewform import messlist
from db_magnit import selectcity
from db_magnit import messtobase
from db_magnit import messread


def app(environ, start_response):
    html = form
    if environ['PATH_INFO'] == '/magnit':
        status = '200 OK'
        response_headers = [('Content-type', 'text/html')]
        start_response(status, response_headers)
        return [html]

    if  environ['PATH_INFO'] == '/view':
        status = '200 OK'
        output = messlist
        response_headers = [('Content-type', 'text/html')]
        start_response(status, response_headers)
        return [output]

    if environ['PATH_INFO'] == '/stat':
        status = '200 OK'
        output = messstat
        response_headers = [('Content-type', 'text/html')]
        start_response(status, response_headers)
        return [output]

    if environ['REQUEST_METHOD'] == 'POST' and environ['PATH_INFO'] == '/statistic':
        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''
        post = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=post_env,
            keep_blank_values=True
        )
        if post['stat'].value:
            regstatistic=regstat()
            output = json.dumps(regstatistic)
            start_response('200 OK', [('Content-Type', 'text/html')])
            return [output]

    if environ['REQUEST_METHOD'] == 'POST' and environ['PATH_INFO'] == '/statcity':
        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''
        post = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=post_env,
            keep_blank_values=True
         )
        if post['statcity'].value:
            statcity=json.loads(post['statcity'].value)
            regstatistic = citystat(statcity)
            output = json.dumps(regstatistic)
            start_response('200 OK', [('Content-Type', 'text/html')])
            return [output]

    if environ['REQUEST_METHOD'] == 'POST' and environ['PATH_INFO'] == '/mess':
        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''
        post = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=post_env,
            keep_blank_values=True
            )
        if post['mess'].value:
            output=messread()
            start_response('200 OK', [('Content-Type', 'text/html')])
            return [output]

    if environ['REQUEST_METHOD'] == 'POST' and environ['PATH_INFO'] == '/delmess':
        
        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''
        post = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=post_env,
            keep_blank_values=True
        )
        messid=post['messdel'].value
        messdelfrombase(messid)
        output="Комментарий удален"
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [output]
    
    if environ['REQUEST_METHOD'] == 'POST' and environ['PATH_INFO'] == '/magnitsmg':
        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''
        post = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=post_env,
            keep_blank_values=True
        )
        mess=post['mess'].value
        messtobase(mess)
        output="Спасибо за комментарий!"
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [output]
    
    if environ['REQUEST_METHOD'] == 'POST' and environ['PATH_INFO'] == '/magnitcity':
        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''
        post = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=post_env,
            keep_blank_values=True
        )
        reg=json.loads(post['region'].value)
        ooooo=selectcity(reg)
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [ooooo]

if __name__ == '__main__':
    try:
        from wsgiref.simple_server import make_server
        httpd = make_server('', 8088, app)
        print('Serving on port 8088...')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Goodbye.')  


