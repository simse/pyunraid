import re

from bs4 import BeautifulSoup

from pyunraid.models.container import Container


def _containers(u):
    # Parse containers page
    soup = BeautifulSoup(
        u.get(
            '/plugins/dynamix.docker.manager/include/DockerContainers.php'
        ).text,
        'lxml'
    )
    containers = []

    # Loop through each table row
    for container in soup.select('tr.sortable'):
        c = Container()

        # Get container name
        c.name = container.find(class_="exec").text.strip()

        # Get container state
        c.state = container.find(class_="state").text.strip()

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
            .replace('-', '_') \
            .replace(' ', '_')

        # Get image tag
        c.tag = container.find(class_="updatecolumn") \
            .find_all("div")[1] \
            .text \
            .strip()

        # Find network
        c.network = container.find_all('td')[2].text.strip()

        # Find port mappings
        span = str(container.find_all('td')[3].find_all('span')[0])
        span = span.replace('<span class="docker_readmore">', '')
        span = span.replace('</span>', '')

        for group in span.split('<br/>'):
            port_mapping = []

            for ip in group.split(
                '<i class="fa fa-arrows-h" style="margin:0 6px"></i>'
            ):
                port_mapping.append(int(re.findall(r':([0-9]{1,5})', ip)[0]))

            c.port_mappings.append(port_mapping)

        # Find path mappings
        span = str(container.find_all('td')[4].find_all('span')[0])
        span = span.replace('<span class="docker_readmore">', '')
        span = span.replace('</span>', '')

        for group in span.split('<br/>'):
            path_mapping = []

            for path in group.split(
                '<i class="fa fa-arrows-h" style="margin:0 6px"></i>'
            ):
                path_mapping.append(path.strip())

            c.path_mappings.append(path_mapping)

        # Find startup delay
        c.startup_delay = container.find_all('td')[6] \
            .find_all('input')[1]['value']

        if not c.startup_delay:
            c.startup_delay = 0

        # Find uptime
        uptime = re.search(
            r'Uptime ([0-9]{1,3}) (hours|days|weeks)',
            container.find_all('td')[7].find_all('div')[0].text
        )

        if not uptime:
            c.uptime = 0
        else:
            match = uptime[0].replace('Uptime ', '')

            c.uptime = _human_to_machine_time(match)

        # Find age
        age = re.search(
            r'Created ([0-9]{1,3}) (hours|days|weeks)',
            container.find_all('td')[7].find_all('div')[1].text
        )

        if not age:
            c.age = 0
        else:
            match = age[0].replace('Created ', '')

            c.age = _human_to_machine_time(match)

        # Find container image
        c.image = container.find('img')['src']

        # Find Dockerhub url
        c.dockerhub_url = container.find_all('a')[1]['href']

        c._set_unraid(u)

        containers.append(c)

    return containers


def _human_to_machine_time(input):
    if 'hours' in input:
        return int(input.replace(' hours', ''))

    if 'days' in input:
        return int(input.replace(' days', '')) * 24

    if 'weeks' in input:
        return int(input.replace(' weeks', '')) * 24 * 7

    if 'months' in input:
        return int(input.replace(' months', '')) * 24 * 7 * 30

    return 0
