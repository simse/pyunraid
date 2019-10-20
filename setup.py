import setuptools
from distutils.core import setup
setup(
  name = 'pyunraid',         # How you named your package folder (MyLib)
  packages = setuptools.find_packages(),   # Chose the same as "name"
  version = '0.4.1',      # Start with a small number and increase it with every change you make
  license='GNU GPLv3',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A Python library to interface directly with Unraid servers',   # Give a short description about your library
  author = 'Simon Sorensen',                   # Type in your name
  author_email = 'hello@simse.io',      # Type in your E-Mail
  url = 'https://github.com/simse/pyunraid',   # Provide either the link to your github or to your website
  keywords = ['unraid', 'control', 'webgui'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests',
          'beautifulsoup4',
          'timefhuman',
          'lxml'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
