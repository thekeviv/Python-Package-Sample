# Import needed function from setuptools
from setuptools import setup

# Create proper setup to be used by pip
setup(name='text_analyzer',
      version='0.0.1',
      description='Perform and visualize a text anaylsis.',
      author='Vivek Sharma',
      packages=['text_analyzer']
	  install_required=['matplotlib',
	  'numpy==1.1.4',
	  'setuptools']
	  )