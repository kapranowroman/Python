# coding: utf-8
import cgi
import sys
import os
import json
import pdb;

from commentForm import form
from db_magnit import messdelfrombase
from messviewform import messlist
from db_magnit import selectcity
from db_magnit import messtobase



def app(environ, start_response):
    html = form
    if environ['PATH_INFO'] == '/magnit':
        status = '200 OK'
        #output = 'обращение по /magnit'
        response_headers = [('Content-type', 'text/html')]
        start_response(status, response_headers)
        return [html]

    if  environ['PATH_INFO'] == '/view':
        status = '200 OK'
        output = messlist
        response_headers = [('Content-type', 'text/html')]
        start_response(status, response_headers)
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
        #mess=json.loads(post['mess'].value)
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
        
        #reg = post['region'].value
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


