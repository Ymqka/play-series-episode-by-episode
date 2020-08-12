from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='medcon-cryacrya',
    version='1.2',
    description='play series episode by episode',
    install_requires=requirements,
    python_requires='>=3.6',
    packages=setuptools.find_packages(),
    scripts=['scripts/medcon']
)