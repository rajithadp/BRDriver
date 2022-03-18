from setuptools import setup, find_packages


setup(
    name='BRDriver',
    version='1',
    license='MIT',
    author="Rajitha Perera",
    author_email='rajithadp@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='example project',
    install_requires=[
          'PySimpleGUI','requests','pandas','Orange','pickle',
      ],

)
