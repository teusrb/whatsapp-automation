from twilio.rest import Client 
import requests
import json

 
account_sid = '[Account_Sid]' 
auth_token = '[Auth_Token]' 
client = Client(account_sid, auth_token) 

requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
cotacao = json.loads(requisicao.text)
valor = float((cotacao['USD'] ['high']))

def send_message(): 
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='A cotação atual do dólar é de R$ {:.2f}'.format(valor),      
                              to='whatsapp:+5511980283113' 
                          ) 
 
    print(message.sid)
