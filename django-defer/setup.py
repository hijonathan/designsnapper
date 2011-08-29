from setuptools import setup, find_packages

DESCRIPTION = 'Abstract API for deferring function execution'
LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.rst').read()
except:
    pass

setup(name='django-defer',
      version='0.2',
      packages=find_packages(),
      author='Waldemar Kornewald',
      author_email='wkornewald@gmail.com',
      url='http://www.allbuttonspressed.com/projects/django-defer',
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      platforms=['any'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Application Frameworks',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'License :: OSI Approved :: BSD License',
      ],
)
