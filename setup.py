from setuptools import find_packages, setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    author='David Carbajosa-Tesoro',
    author_email='david.carbajosa@pleyadesltd.com',
    description='A utility for backing up PostgreSQL DBs',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/dcedyga/pgbackup.git',
    packages=find_packages('src')
)