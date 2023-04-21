from setuptools import setup

from BelDHAnalyser import __version__

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

setup(
    version=__version__,
    name='bel-digital-handwriting-py',
    description='Пакет для аналіза беларускіх тэкстаў і вызначэння лічбавага почырку пісьменніка',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/Kononenko-Daniil/bel-digital-handwriting-py',
    author='Daniil Kononenko',
    package_dir={'BelDHAnalyser': 'BelDHAnalyser'},
    packages=['BelDHAnalyser'],
    license="MIT",
    project_urls={
        "Source": "https://github.com/Kononenko-Daniil/bel-digital-handwriting-py"
    }
)
