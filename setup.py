from setuptools import setup, find_packages

setup(
    name='outsource',
    version='0.0.1',
    description='manage aws spot instances',
    url='https://github.com/frnsys/outsource',
    author='Francis Tseng (@frnsys)',
    author_email='f@frnsys.com',
    license='MIT',

    packages=find_packages(),
    install_requires=[
        'click',
        'colorama',
        'pyyaml',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        outsource=outsource:cli
    ''',
)