from distutils.core import setup
setup(
  name='tuxanonymizer',
  packages=['tuxanonymizer'],   # Chose the same as "name"
  version='0.2',
  license='MIT',
  description='Customer file obfuscation library and cli',
  author='Francois CADEILLAN',
  author_email='narfai@azsystem.fr',
  url='https://github.com/narfai/tuxanonymize',
  download_url='https://github.com/narfai/tuxanonymize/archive/v_02.tar.gz',
  keywords=['ANONYMIZE', 'OBFUSCATION', 'CUSTOMER', 'XML'],
  install_requires=[
      'xmltodict',
  ],
  scripts=['bin/tuxanonymizer'],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
