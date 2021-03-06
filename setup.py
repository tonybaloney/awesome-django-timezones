#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_version(*file_paths):
    """Retrieves the version from awesome_django_timezones/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


version = get_version("awesome_django_timezones", "__init__.py")


if sys.argv[-1] == 'publish':
    try:
        import wheel
        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist bdist_wheel')
    os.system('python -m twine upload dist/*')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on git:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='awesome-django-timezones',
    version=version,
    description='Easily set a localized timezone for users',
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/x-rst',
    author='Will Gordon',
    author_email='will@gordoncode.com',
    url='https://github.com/wgordon17/awesome-django-timezones',
    packages=[
        'awesome_django_timezones',
    ],
    include_package_data=True,
    install_requires=[
        'ipapi',
        'django>=2.1'
    ],
    license='MIT',
    zip_safe=False,
    keywords='awesome-django-timezones',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    project_urls={
        'Documentation': 'https://awesome-django-timezones.readthedocs.io',
        'Source': 'https://github.com/wgordon17/awesome-django-timezones',
    },
)
