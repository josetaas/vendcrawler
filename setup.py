from codecs import open as codecs_open
from setuptools import setup, find_packages


setup(name='vendcrawler',
      version='0.0.1',
      classifiers=[],
      url='https://github.com/josetaas/vendcrawler',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click',
          'pymysql'
      ],
      extras_require={
          'test': ['pytest'],
      },
      entry_points="""
      [console_scripts]
      vendcrawler=vendcrawler.scripts.cli:cli
      """
      )
