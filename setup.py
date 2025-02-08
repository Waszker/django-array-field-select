import pathlib

from setuptools import setup

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name='django-array-field-select-multiple',
    version='0.3.2',
    description=(
        'A replacement for Django\'s ArrayField with a multiple '
        'select form field.'
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Piotr Waszkiewicz',
    author_email='waszka23@gmail.com',
    license='MIT',
    url='https://github.com/Waszker/django-array-field-select',
    packages=['array_field_select'],
    install_requires=['Django>=1.8'],
    classifiers=[
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 4.1',
        'Framework :: Django :: 4.2',
        'Framework :: Django :: 5.0',
        'Framework :: Django :: 5.1',
        'Programming Language :: Python :: 3',
    ]
)
