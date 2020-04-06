import requests
import json
import time
import argparse
import configparser
import sys

class OceanApi:

    def __init__(self, conf_file='conf.cfg'):
        config = configparser.ConfigParser()
        config.readfp(open(conf_file))
        token = config.get('auth', 'token')
        self.auth_headers = {'Authorization': 'Bearer {}'.format(token),
                             'Content-Type': 'application/json'}

    def droplets(self):
        response = requests.get(url='https://api.digitalocean.com/v2/droplets', headers=self.auth_headers)
        return json.loads(response.text)

    def id_droplet(self):
        response = requests.get(url='https://api.digitalocean.com/v2/droplets', headers=self.auth_headers)
        droplets = json.loads(response.text)
        if droplets['droplets']:
            if len(droplets['droplets']) > 1:
                print('You have more than one droplet')
            return droplets['droplets'][0]['id']
        else:
            return None

    def droplet(self, droplet_id):
        response = requests.get(url='https://api.digitalocean.com/v2/droplets/{}'.format(droplet_id), headers=self.auth_headers)
        return json.loads(response.text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--status', action='store_true', dest='status', default=False)

    args = parser.parse_args()
    api = OceanApi()
    if args.status:
        droplet_id = api.id_droplet()
        if droplet_id:
            _droplet = api.droplet(droplet_id)['droplet']
            print('DROPLET: {}, STATUS:{}, IP:{}, REGION: {}, DIST: {}'.format(_droplet['name'], _droplet['status'].upper(), _droplet['networks']['v4'][0]['ip_address'], _droplet['region']['slug'].upper(), _droplet['image']['slug']))
        else:
            print('No droplets')
