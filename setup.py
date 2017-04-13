from setuptools import setup

setup(
    name='sort-algorithms',
    version='1.0.1',
    packages=['sort',],
    license='MIT',
    description='Sorting algorithms written in and made for Python lists and tuples',
    long_description=open('README.rst').read(),
    author='Florian Dahlitz',
    author_email='f2dahlitz@freenet.de',
    url='https://github.com/DahlitzFlorian/SortingAlgorithms',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='sort algorithms sorting lists tuples',
)