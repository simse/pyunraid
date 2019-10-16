import re

import requests
from bs4 import BeautifulSoup

from pyunraid.helpers import *
from pyunraid.constants import *
from pyunraid.models.container import Container


def containers(u):

    return parse_containers(u)


def parse_containers(u):
    # Parse containers page
    soup = BeautifulSoup(u.get('/plugins/dynamix.docker.manager/include/DockerContainers.php').text, 'lxml')
    containers = []

    # Loop through each table row
    for container in soup.select('tr.sortable'):
        c = Container()

        # Get container name
        c.name = container.find(class_="exec").text

        # Get container state
        c.state = container.find(class_="state").text

        # Get container ID
        c.id = re.findall(
            r'[A-Z,a-z,0-9]{12}',
            container.find(class_="advanced").text
        )[0]

        # Get container update status
        c.update_status = container.find(class_="updatecolumn") \
            .find("span") \
            .text \
            .strip() \
            .upper() \
            .replace('-', '_')


        # Get image tag
        c.tag = container.find(class_="updatecolumn") \
            .find_all("div")[1] \
            .text \
            .strip()

        # Find network
        c.network = container.find_all('td')[2].text

        # Find port mappings
        span = str(container.find_all('td')[3].find_all('span')[0])
        span = span.replace('<span class="docker_readmore">', '')
        span = span.replace('</span>', '')

        for group in span.split('<br/>'):
            port_mapping = []

            for ip in group.split('<i class="fa fa-arrows-h" style="margin:0 6px"></i>'):
                port_mapping.append(re.findall(r':([0-9]{1,5})', ip)[0])

            c.port_mappings.append(port_mapping)

        # Find path mappings
        span = str(container.find_all('td')[4].find_all('span')[0])
        span = span.replace('<span class="docker_readmore">', '')
        span = span.replace('</span>', '')

        for group in span.split('<br/>'):
            path_mapping = []

            for path in group.split('<i class="fa fa-arrows-h" style="margin:0 6px"></i>'):
                path_mapping.append(path)

            c.path_mappings.append(path_mapping)

        # Find startup delay
        c.startup_delay = container.find_all('td')[6].find_all('input')[1]['value']

        # Find uptime
        uptime = re.search(r'Uptime ([0-9]{1,3})', \
            container.find_all('td')[7].find_all('div')[0].text)

        if not uptime:
            c.uptime = 0
        else:
            c.uptime = uptime[0].replace('Uptime ', '')

        # Find age
        age = re.search(r'Created ([0-9]{1,3})', \
            container.find_all('td')[7].find_all('div')[1].text)

        if not age:
            c.age = 0
        else:
            c.age = age[0].replace('Created ', '')

        # Find container image
        c.image = container.find('img')['src']

        # Find Dockerhub url
        c.dockerhub_url = container.find_all('a')[1]['href']

        c.unraid = u

        containers.append(c)


    return containers
