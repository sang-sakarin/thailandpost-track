from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='thailandpost-track',
    version='1.0.0',
    description='A Python library for Thailand Post track API',
    long_description=readme(),
    long_description_content_type="text/markdown",
    url='https://github.com/sang-sakarin/thailandpost-track',
    author='sang_sakarin',
    author_email='sang_sakarin@outlook.com',
    license='sang_sakarin',
    scripts=[],
    keywords='thailandport-track thailandport-track-python',
    packages=['thailandpost_track'],
    install_requires=['requests'],
)
