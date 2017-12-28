from setuptools import setup, find_packages

setup(
	name = "licor",
	version = "0.0.1",
	packages = find_packages(),
	package_data = {"licor": ["templates/*"]},
	author = "Daniel Knüttel",
	author_email = "daniel.knuettel@daknuett.eu",
	install_requires = ["docopt"]

     )
