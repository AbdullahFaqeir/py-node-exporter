from setuptools import setup, find_packages

from py_node_exporter.py_node_exporter import __version__

setup(
    name="py_node_exporter",
    version=__version__,
    packages=find_packages(),
    install_requires=['prometheus_client'],
    author='Abdullah Al-Faqeir',
    author_email='abdullah@devloops.net'
)
