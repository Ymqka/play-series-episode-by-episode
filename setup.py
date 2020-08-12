from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
   name='medcon',
   version='1.0',
   description='play series episode by episode',
   install_requires=requirements,
   python_requires='>=3.6',
)