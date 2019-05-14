# Import needed function from setuptools
from setuptools import setup

# Create proper setup to be used by pip
setup(name='a_python_package',
      version='0.0.1',
      description='a template to create a package in python',
      author='Vivek Sharma',
      packages=['a_python_package'], 
	  install_required=['matplotlib',
	  'numpy==1.1.4',
	  'setuptools']
	  )
