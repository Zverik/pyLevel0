import level0
from setuptools import setup

setup(
    name='level0',
    version=level0.__version__,
    packages=['level0'],
    license='WTFPL',
    description='Console OpenStreetMap Editor',
    author=level0.__author__,
    author_email='ilya@zverev.info',
    url='https://github.com/Zverik/pyLevel0',
    entry_points={
        'console_scripts': [
            'level0 = level0.level0:main',
        ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: System :: Shells',
        'Topic :: Terminals',
        'Topic :: Utilities'
    ],
)
