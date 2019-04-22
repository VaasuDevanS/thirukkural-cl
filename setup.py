from setuptools import setup, find_packages

__version__   = "1.1"

CLASSIFIERS = [
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
]

setup(name='thirukkural',
      entry_points={
          'console_scripts': [
              'thirukkural=thirukkural:main'
          ]
      },
      version=__version__,
      url='https://github.com/VaasuDevanS/thirukkural-cl',
      license='LICENSE.txt',
      author='Vaasudevan Srinivasan',
      author_email='vaasuceg.96@gmail.com',
      description='Thirukkural for command-line and python module',
      packages=find_packages(),
      include_package_data=True,
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      zip_safe=False,
      classifiers=CLASSIFIERS,
 )
