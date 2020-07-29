try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = {
    'description': 'ex48',
    'author': 'Ifedayo Ijabadeniyi',
    'url': 'url to get it at',
    'download url': 'where to download it',
    'author email': 'ifedayoadeniyi@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['folder name'],
    'scripts': [''],
    'name': 'ex48'
}

setup(**config)
