import setuptools
from setuptools import setup


setup(name='trello-kpt',
      version='1.0',
      description='CLI tool for Trello',
      packages=setuptools.find_packages(),
      install_requires=['Click', 'PyYAML', 'py-trello'],
      entry_points={
            'console_scripts': [
                  'trello = commands.cli:main'
            ],
      },
)