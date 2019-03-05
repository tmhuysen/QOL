from setuptools import setup, find_packages

setup(name = 'QOL',
      version = '0.0.1',
      url = 'https://github.com/tmhuysen/QOL',
      license = 'GNU Lesser General Public License v3.0',
      author = 'Tobias Huysentruyt',
      author_email = 'tobias.huysentruyt@minimoa.net',
      description = 'Quality of life',
      packages = find_packages(exclude = ['tests']),
      test_suite = "tests",
      long_description = open('README.md').read(),
      zip_safe = False,
      install_requires = ['numpy'])
