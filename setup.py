import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='relation_extraction',
    version='0.1',
    scripts=['runserver.py'],
    author='@UKPLab, @markmo',
    author_email='',
    description='Context-Aware Representations for Knowledge Base Relation Extraction',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/markmo/emnlp2017-relation-extraction',
    packages=setuptools.find_packages(),
    package_data={'relation_extraction': ['resources/*.txt', 'resources/*.json']},
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
