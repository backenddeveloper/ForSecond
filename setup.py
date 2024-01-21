from os import environ
from setuptools import setup


setup(
    name='forsecond',
    version=environ.get('VERSION', '0.1.0'),

    author='Dr. Graham Turner',
    author_email='grahamturnernew@hotmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Local Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Internal Pasters',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Topic :: Tech Test',
    ],
    copyright='Dr. Graham Turner 2023',
    description='Technical test solutions for second',
    include_package_data=True,
    install_requires=[],
    packages=[
        'forsecond',
    ],
    python_requires='>=3.10',
    test_suite="tests.forsecond",
    url='https://github.com/backenddeveloper/forsecond'
)
