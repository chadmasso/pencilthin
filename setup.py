from distutils.core import setup
setup(
    name = 'pencilthin',
    packages = ['pencilthin', 'pencilthin.management', 'pencilthin.management.commands'],
    package_dir = {'management' : 'management/', 'commands' : 'management/commands/'},
    version = '0.0.1',
    description = 'Handlebars Template Compiler with Django template tag support',
    author = 'Chad Masso',
    author_email = 'chad.m.masso@gmail.com',
    maintainer = 'Chad Masso',
    maintainer_email = 'chad.m.masso@gmail.com',
)
