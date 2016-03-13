from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='scrapazhon',
      version='0.0.1',
      description='Scrape Amazon App Store',
      url='http://github.com/fegoa89',
      author='Fernando Gonzalez Aguilera',
      author_email='fgonzalezaguilera@gmail.com',
      license='MIT',
      packages=['scrapazhon'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'])