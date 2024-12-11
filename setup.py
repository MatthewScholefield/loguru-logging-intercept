from setuptools import setup

with open('README.md', mode='r') as f:
    LONG_DESC = f.read()

setup(
    name='loguru-logging-intercept',
    version='0.1.4',
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
    ],
    keywords=['loguru', 'logging', 'intercept'],
    packages=find_namespace_packages(include=['loguru_logging_intercept*']),
    install_requires=[
        'loguru'
    ],
)
