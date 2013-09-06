from setuptools import setup
the_version='0.1.0'
the_name='pscripts'
scripts = ['scripts/inc-ver']
setup(
    name = the_name,
    version = the_version,
    packages = [the_name],
    description = 'Weechat Notification Plugin',
    author='Fenton Travers',
    author_email='fenton.travers@gmail.com',
    url='www.google.com',
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description='Some description',
    classifiers=[
        'Programming Language :: Python :: 3.3',
    ]
    scripts = scripts
)
