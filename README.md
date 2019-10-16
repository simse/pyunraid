# pyunraid

Pyunraid is a Python library designed to interface directly with an Unraid server
without installing any software on directly on the server.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pyunraid.

```bash
pip install pyunraid
```

## Usage

```python
from pyunraid.unraid import Unraid

# Create Unraid server object
unraid = Unraid('192.168.1.4', 'root', 'your-secure-password')

# Get all Docker containers
containers = unraid.containers()
```

## Documentation
_Since the project is still in its early stages, there may not be documentation for everything._
You may find the documentation on the wiki.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
