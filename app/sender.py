from bottle import route, run, request

@route('/api', method='POST')
def send():    
    return "Email com assunto enviado com sucesso!"

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True)