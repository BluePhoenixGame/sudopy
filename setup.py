from setuptools import setup

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

readme = ''
with open('README.rst') as f:
    readme = f.read()

setup(
    name='sudopy',
    author='Bluenix',
    url='https://github.com/BluePhoenixGame/sudopy',
    project_urls={
        'Issue Tracker': 'https://github.com/BluePhoenixGame/sudopy/issues'
    },
    version='0.0.1',
    packages=['sudopy'],
    license='MIT',
    description='Sudoku solver in Python with efficiency and performance in mind',
    long_description=readme,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    install_requires=requirements,
    python_requires='>=3.6',  # TODO: Verify this
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
