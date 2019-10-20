from bs4 import BeautifulSoup

from pyunraid.models.plugin import Plugin


PLUGIN_UPDATE_STATUS = {
    'up-to-date': 'UP_TO_DATE'
}


def _plugins(u):
    # Parse containers page
    soup = BeautifulSoup(
        u.get(
            '/plugins/dynamix.plugin.manager/include/ShowPlugins.php?check=1'
        ).text,
        'lxml'
    )
    plugins = []

    for plugin in soup.find_all('tr'):
        p = Plugin()

        # Find plugin image
        if plugin.find('img'):
            p.image = plugin.find('img')['src']

        else:
            p.image = 'icon:' + plugin.find('i')['class'][1]

        # Find plugin name and description
        if plugin.select('.desc_readmore h4'):
            p.name = plugin.select('.desc_readmore h4')[0].text
            p.description = plugin.select('.desc_readmore p')[0].text

        else:
            p.name = plugin.select('.desc_readmore strong')[0].text
            p.description = plugin.select('.desc_readmore p')[1].text

        # Find plugin support thread
        p.support_thread = plugin.find_all('a')[1]['href']

        # Find plugin author
        p.author = plugin.find_all('td')[2].text

        # Find plugin version
        p.version = plugin.find_all('td')[3].text

        # Find plugin update status
        p.update_status = PLUGIN_UPDATE_STATUS[plugin.find_all('td')[4].text]

        p._set_unraid(u)

        plugins.append(p)

    return plugins
