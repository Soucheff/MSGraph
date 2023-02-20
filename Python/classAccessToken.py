import json
from datetime import datetime,timedelta
from msal import ConfidentialClientApplication

class Token:
    scope = ['https://graph.microsoft.com/.default']
    clientId = ""
    clientSecret = ""
    accessToken = ""
    authorityUrl = ""
    bearerToken = ""
    exp = datetime.now()-timedelta(hours=-1)

    def __init__(self):
        with open('config.json') as f:
            config = json.load(f)
        self.authorityUrl = ('https://login.microsoftonline.com' + '/' + config['tenant'])
        self.clientId = config['clientId']
        self.clientSecret = config['clientSecret']
        self.getAccessToken()
    
    def getAccessToken(self):
        client = ConfidentialClientApplication(client_id=self.clientId,authority=self.authorityUrl,client_credential=self.clientSecret)
        token_result = client.acquire_token_silent(self.scope, account=None)
        
        if token_result:
            print('Access token was loaded from cache')

        if not token_result:
            token_result = client.acquire_token_for_client(scopes=self.scope)
            print('New access token was acquired from Azure AD')

        self.bearerToken = 'Bearer ' + token_result['access_token']
        self.accessToken = token_result['access_token']
        self.exp = datetime.now() + timedelta(seconds=token_result['expires_in']-60)
        return
        
    def tokenIsValid(self):
        if self.exp <= datetime.now():
            return False
        else:
            return True

if __name__ == "__main__":
    
    token = Token()
    token.getAccessToken()
    print(token.accessToken)
    print(token.exp)
