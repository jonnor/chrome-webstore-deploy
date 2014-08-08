import os

from setuptools import setup

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
    name='chrome-webstore-deploy',
    version='0.0.2',
    description='Automate deployment of Chrome extensions/apps to Chrome Web Store.',
    long_description=(read('README.rst') + '\n\n'),
    url='http://github.com/jonnor/chrome-webstore-deploy/',
    license='MIT',
    author='Jon Nordby',
    author_email='jononor@gmail.com',
#    py_modules=['foo'],
    scripts=['bin/chrome-web-store.py'],
    install_requires=[
        "oauth2client >= 1.2",
        "httplib2 >= 0.9",
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
