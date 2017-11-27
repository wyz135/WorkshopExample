from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='WorkshopExample',
      version='0.0.1',
      description='Random example project for coding workshop',
      url='http://github.com/Samreay/WorkshopExample',
      author='Samuel Hinton',
      author_email='samuelreay@gmail.com',
      license='MIT',
      install_requires=requirements,
      packages=find_packages(exclude=('tests', 'doc'))
      )
