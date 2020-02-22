from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='sqlalchemy.dbapi',
      version=version,
      description="a site policy for qyxycjh web site",
      long_description=open("README.md").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='python plone',
      author='Adam tang',
      author_email='568066784@qq.com',
      url='https://github.com/adam139/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['sqlalchemy'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.CMFPlone',      
          'SQLAlchemy',    
          'mysqlclient==1.4.6',
          'MySQL-python',
#           'cx_Oracle == 5.2.1',                    
          'collective.autopermission',
                                                                     
          # -*- Extra requirements: -*-
      ],
      extras_require={
          'test': ['plone.app.testing',]
      },         
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,

      )
