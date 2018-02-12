#from setuptools import setup
from distutils.core import setup

setup(
      name='bijoy2unicode',
      version='0.1.0',
      description='Convert text/file written in Bijoy to Unicode',
      url='http://github.com/mad-fox/bijoy2unicode',
      download_url = 'http://github.com/mad-fox/bijoy2unicode/archive/0.1.0.tar.gz',
      author='Rajib Biswas',
      author_email='sarb.rb@gmail.com',
      license='MIT',
      packages=['bijoy2unicode'],
      zip_safe=False,
      keywords = ['bengali', 'bangla', 'nlp', 'bijoy', 'avro', 'unicode'],
      classifiers = []
)