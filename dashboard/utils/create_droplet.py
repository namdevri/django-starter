import requests
import json
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 8843f6e5f466e3302f37bc5ebcaa70ce17b9a73bc6f5126ea66cb4502a1d353e',
}
data = {
    'name': 'clientblahblah',
    'region': 'nyc1',
    'size': 's-1vcpu-1gb',
    'image': '50196257'
}
r = requests.post('https://api.digitalocean.com/v2/droplets', data=json.dumps(data), headers=headers)
print(r.status_code)
print(r.text)
