import os
from setuptools import setup

module_path = os.path.join(os.path.dirname(__file__), 'flask_djangoquery.py')
version_line = [line for line in open(module_path)
                if line.startswith('__version_info__')][0]

__version__ = '.'.join(eval(version_line.split('__version_info__ = ')[-1]))

setup(name='Flask-DjangoQuery',
      version=__version__,
      url='https://github.com/messense/Flask-DjangoQuery',
      license='MIT',
      author='Messense Lv',
      author_email='messense@icloud.com',
      description='Django like query for Flask-SQLAlchemy',
      py_modules=['flask_djangoquery'],
      zip_safe=False,
      platforms='any',
      install_requires=open("requirements.txt").readlines(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ])
