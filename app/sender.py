import pyscopg2
from bottle import route, run, request

DSN = 'dbname=email_sender user=postgres host=db'
SQL = 'INSERT INTO emails (assunto, mensagem) VALUES (%s, %s)'

def register_email(assunto, mensagem):
    try:
        conn = pyscopg2.connect(DSN)
        cursor = conn.cursor()
        cursor.execute(SQL, (assunto, mensagem))
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()
        print("Email registrado!")

@route('/api', method='POST')
def send():   
    assunto = request.forms.get('assunto')
    mensagem = request.forms.get('mensagem')

    register_email(assunto, mensagem)
    return "Email com assunto enviado com sucesso!"

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True)