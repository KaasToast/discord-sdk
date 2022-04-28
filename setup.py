from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='discord-sdk',
    author='KaasToast',
    url='https://github.com/KaasToast/discord-sdk.py',
    version='V1',
    packages=['discord-sdk'],
    license='MIT',
    description='A debug/utility extension for Discord bots. Made for Pycord.',
    include_package_data=True,
    install_requires=requirements
)