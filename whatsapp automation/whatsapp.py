from twilio.rest import Client 
import requests
import json

 
account_sid = 'ACcdfced11262290327b9aa6a83f72bfa2' 
auth_token = '912957d344b52a9eb3d5f5355b956703' 
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