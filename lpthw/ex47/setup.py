try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = {
    'description': 'ex47',
    'author': 'Ifedayo Ijabadeniyi',
    'url': 'url to get it at',
    'download url': 'where to download it',
    'author email': 'ifedayoadeniyi@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': ['bin/game.py'],
    'name': 'game.py'
}

setup(**config)
