from setuptools import setup

setup(
    name='weatherallapi',
    version='0.1',
    author_email='c7982792@gmail.com'
    packages=['weatherallapi'],
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'weatherallapi = weatherallapi.weatherallapi:main',
        ],
    },
)