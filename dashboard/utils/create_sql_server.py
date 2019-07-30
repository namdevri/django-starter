import requests
import json
import time

client_id = '9a0f25aa-37ed-4ed3-9f17-4348a3a86635'
client_secret = '00a:ezx@S]*huJ3y5lt-ft6z63QnalQS'
subscription_id = '291d1e07-116b-4e42-a929-c470e52ab1b3'
def get_access_token():
    data = {
      'grant_type': 'client_credentials',
      'client_id': client_id,
      'client_secret': client_secret,
      'resource': 'https://management.azure.com/'
    }

    r = requests.post('https://login.microsoftonline.com/ceed4836-523d-4490-9ead-8d859e78e938/oauth2/token', data=data)
    return json.loads(r.text)['access_token']

def list_sql_servers():
    token = get_access_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    resp = requests.get(url=f'https://management.azure.com/subscriptions/{subscription_id}/resourceGroups/api-ease/providers/Microsoft.Sql/servers?api-version=2015-05-01-preview', headers=headers).json()['value']
    return [i['name'] for i in resp]
def create_database(server_name, database_name):
    token = get_access_token()
    data = {
        "location": "East US"
    }
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    r = requests.put(url=f'https://management.azure.com/subscriptions/{subscription_id}/resourceGroups/api-ease/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}?api-version=2017-10-01-preview', data=json.dumps(data), headers=headers)
    print(r.status_code)
    print(r.text)
def create_sql_server(name):
    token = get_access_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    data = {
      "properties": {
        "administratorLogin": "engineering",
        "administratorLoginPassword": "Un53cuRE!"
      },
      "location": "East US"
    }
    url = f'https://management.azure.com/subscriptions/{subscription_id}/resourceGroups/api-ease/providers/Microsoft.Sql/servers/{name}?api-version=2015-05-01-preview'
    r = requests.put(url, data=json.dumps(data), headers=headers)
    attempts = 12
    while attempts > 0:
        if name in list_sql_servers():
            create_database(name, 'testdb')
            print('testdb created')
            break
        else:
            print('dne')
            attempts -= 1
            time.sleep(10)

create_sql_server('systemtest')
