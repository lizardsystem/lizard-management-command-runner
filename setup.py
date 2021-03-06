from setuptools import setup

version = '0.4.dev0'

long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CREDITS.rst').read(),
    open('CHANGES.rst').read(),
    ])

install_requires = [
    'Django >= 1.9, < 2',
    'celery >= 4',
    'lizard-ui',
    ],

tests_require = [
    'nose',
    'coverage',
    'mock',
    'factory_boy',
    'django-nose',
    ]

setup(name='lizard-management-command-runner',
      version=version,
      description="Run management commands from a protected web page",
      long_description=long_description,
      # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Programming Language :: Python',
                   'Framework :: Django',
                   ],
      keywords=[],
      author='Remco Gerlich',
      author_email='remco.gerlich@nelen-schuurmans.nl',
      url='',
      license='GPL',
      packages=['lizard_management_command_runner'],
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require={'test': tests_require},
      entry_points={
          'console_scripts': [
          ]},
      )
