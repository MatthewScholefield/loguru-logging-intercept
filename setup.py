from setuptools import setup

with open('README.md', mode='r') as f:
    LONG_DESC = f.read()

setup(
    name='loguru-logging-intercept',
    version='0.1.5',
    description='Code to integrate Loguru with Python\'s standard logging module',
    long_description=LONG_DESC,
    long_description_content_type='text/markdown',

    url='https://github.com/MatthewScholefield/loguru-logging-intercept',
    author='Matthew D. Scholefield',
    author_email='matthew331199@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
    keywords='loguru logging intercept',
    py_modules=['loguru_logging_intercept'],
    install_requires=[
        'loguru'
    ],
)
