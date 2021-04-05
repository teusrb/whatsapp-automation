from twilio.rest import Client 
import requests
import json
import time


 
account_sid = '[Account_Sid]' 
auth_token = '[Auth_Token]' 
client = Client(account_sid, auth_token) 

requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL,EUR-BRL')
cotacao = json.loads(requisicao.text)
valor_dolar = float((cotacao['USD'] ['high']))
valor_euro = float((cotacao['EUR'] ['high']))

hora = time.strftime('%d/%m/%y %H:%M', time.localtime())


def send_message(): 
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='A cotação atual do dólar é de R$ {:.2f} \nA cotação atual do Euro é de R$ {:.2f} \nA data e horário dessa consulta foram: {}'.format(valor_dolar, valor_euro, hora),      
                              to='whatsapp:+5511980283113' 
                          ) 
 
    print(message.sid)
