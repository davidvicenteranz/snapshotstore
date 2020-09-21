from distutils.core import setup
from snapshotstore import __version__, __author__

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='snapshotstore',
    version=__version__,
    packages=['snapshotstore'],
    url='https://github.com/davidvicenteranz/snapshotstore',
    license='MIT License',
    author=__author__,
    author_email='dvicente74@gmail.com',
    description='Python 3 snapshot store using filesystem',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ],
    long_description=long_description,
    install_requires=[
        'evnthandler'
    ]
)