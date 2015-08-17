from setuptools import setup, find_packages


setup(
    name='hexapod',
    description='A high-level interface for the ArcBotics Hexy robot',
    url='https://github.com/mluds/hexapod',
    author='Michael Ludwig',
    author_email='mluds@ymail.com',
    packages=find_packages(),
    install_requires=['pyserial', 'PyYaml'],
    include_package_data=True
)