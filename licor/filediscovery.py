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



import glob, os

def discover_this_path(path, file_ending, root_path = ""):
	"""
	Discover all matching files in this path.

	Return an iterator yielding the filepaths.
	"""

	if(not root_path):
		root_path = os.curdir

	return (os.path.relpath(os.path.abspath(p), root_path) 
			for p in glob.iglob(os.path.join(path, "*." + file_ending)))


def discover_all(path, file_ending, ignore_paths = []):
	"""
	Discover all matching files in this path and
	all subpaths.

	Yield the filepaths.
	"""
	root_path = os.path.abspath(path)
	
	for p in os.walk(path):
		path = p[0]
		splitted = path.split(os.sep)

		if(any( [ignore in splitted for ignore in ignore_paths ])):
			continue
		
		for i in discover_this_path(path, file_ending, root_path = root_path):
			yield i


	
