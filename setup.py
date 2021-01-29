from setuptools import setup

setup(
    name='loguru-logging-intercept',
    version='0.1.0',
    description='Code to integrate Loguru with Python\'s standard logging module',
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
    ],
    keywords='loguru logging intercept',
    py_modules=['loguru_logging_intercept'],
    install_requires=[
        'loguru'
    ],
)
