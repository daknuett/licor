# Copyright (c) 2018 Daniel Knüttel                                           #
#                                                                             #
# This file is part of licor.                                                 #
#                                                                             #
# licor is free software: you can redistribute it and/or modify               #
# it under the terms of the GNU Affero General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or           #
# (at your option) any later version.                                         #
#                                                                             #
# licor is distributed in the hope that it will be useful,                    #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
# GNU General Public License for more details.                                #
#                                                                             #
# You should have received a copy of the GNU Affero General Public License    #
# along with licor.  If not, see <http://www.gnu.org/licenses/>.              #
#                                                                             #
#                                                                             #

from setuptools import setup, find_packages

setup(
	name = "licor",
	version = "0.0.4",
	packages = find_packages(),
	package_data = {"licor": ["templates/*", "templates/*/*"]},
	author = "Daniel Knüttel",
	author_email = "daniel.knuettel@daknuett.eu",
	url = "https://github.com/daknuett/licor",
	install_requires = ["docopt"],
	description = "A script to add license disclaimers",
	long_description = open("README.rst").read(),

	entry_points = {"console_scripts": ["licor = licor.main:main"]}
     )
