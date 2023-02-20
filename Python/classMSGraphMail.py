from classAccessToken import Token
import requests
import json


class MSGraphMail:
    _token: Token
    _email=""

    def __init__(self,email):
        self._token = Token()
        self.change_email(email)
        return

    def change_email(self,email):
        self._email = email
        return email

    def get_user_messages(self):
        endpoint = ("https://graph.microsoft.com/v1.0/users/{0}/messages?$select=sender,subject,sentDateTime,bodyPreview").format(self._email)
        if not self._token.tokenIsValid():
            self._token.getAccessToken()
        
        headers = {
            'Authorization': ('Bearer {0}').format(self._token.accessToken)
        }


        try:
            messages = requests.get(url=endpoint,headers=headers).json()
            print("*************************************************** Messages ******************************************************\n")
            for msg in messages['value']:
                print('from: {2} | Subject: {0} | Body Preview: {1} | Date Received: {3}'.format(msg['subject'], msg['bodyPreview'],msg['sender'],msg['sentDateTime']))
                print("========================================================================================================================================\n")

            print("***************************************************** End Messages ************************************************************\n")
        except Exception as e:
            print(e.error.message)
        

    def get_token(self):
        print(self._token.accessToken)
        print("Expiration: ",self._token.exp)
    
    def send_mail(self, subject: str, body: str, recipient: str):
        endpoint = ("https://graph.microsoft.com/v1.0/users/{0}/sendMail").format(self._email)
        if not self._token.tokenIsValid():
            self._token.getAccessToken()
        
        headers = {
            'Authorization': ('Bearer {0}').format(self._token.accessToken),
            'Content-Type': 'application/json'
        }

        json_body = {
            'message': {
                'subject': subject,
                'body': {
                    'contentType': "Text",
                    'content': body
                },
                'toRecipients':[
                    {
                        'emailAddress': {
                            'address': recipient
                        }
                    }
                ]
            },
            'saveToSentItems': True
        }

        r = requests.post(url=endpoint,headers=headers,data=json.dumps(json_body))
        print(r.text)