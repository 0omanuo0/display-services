from flask import Flask
import requests
import time
import threading as th
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
api_token_proxmox = os.getenv('API_TOKEN_PROXMOX')

# remove warning insecure request
requests.packages.urllib3.disable_warnings()

services = {
    'portfolio': 'https://10.1.1.101:7443',
    'homeassistant': 'http://10.1.1.99:8123',
    'crafty' : 'https://10.1.1.101:8443',
    'pihole': 'http://10.1.1.101:80',
}

service_status = [] # {service_name: {elapsed_time: 0, response_code: 200, status: 'up'}}

def loopServices():
    global service_status
    while True:
        service_status = []
        for service in services:
            try:
                data = requests.get(services[service], verify=False, timeout=5)
                if service not in service_status:
                    service_status.append({
                            'name': service,
                            'elapsed_time': data.elapsed.total_seconds(),
                            'response_code': data.status_code,
                            'status': 'up'
                    })
            except Exception as e:
                if service not in service_status:
                    service_status.append({
                            'name': service,
                            'elapsed_time': 0,
                            'response_code': 0,
                            'status': 'down'
                    })
        print(f'[INFO] Updated services status')
        time.sleep(60)



@app.route('/status')
def status():
    data = {}
    dataNode = requests.get(
        'https://proxmox.local:8006/api2/json/nodes/server-manu/status', 
        verify=False, 
        headers={'Authorization': f'PVEAPIToken=root@pam!prueba1={api_token_proxmox}'}
    )

    dataContainers = requests.get(
        'https://proxmox.local:8006/api2/json/nodes/server-manu/lxc', 
        verify=False, 
        headers={'Authorization': f'PVEAPIToken=root@pam!prueba1={api_token_proxmox}'}
    )

    dataVM = requests.get(  
        'https://proxmox.local:8006/api2/json/nodes/server-manu/qemu', 
        verify=False, 
        headers={'Authorization': f'PVEAPIToken=root@pam!prueba1={api_token_proxmox}'}
    )

    data['node'] = dataNode.json()['data']
    data['containers'] = dataContainers.json()['data']
    data['vm'] = dataVM.json()['data']
    data['services'] = service_status


    return data, 200, {'Access-Control-Allow-Origin': '*'}


if __name__ == '__main__':
    th.Thread(target=loopServices).start()
    app.run(host='0.0.0.0', port=5000, debug=True)