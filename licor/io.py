import os

#
# Copyright(c) Daniel Knüttel
#

# This program is free software.
# Anyways if you think this program is worth it
# and we meet shout a drink for me.


#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    Dieses Programm ist Freie Software: Sie können es unter den Bedingungen
#    der GNU Affero General Public License, wie von der Free Software Foundation,
#    Version 3 der Lizenz oder (nach Ihrer Wahl) jeder neueren
#    veröffentlichten Version, weiterverbreiten und/oder modifizieren.
#
#    Dieses Programm wird in der Hoffnung, dass es nützlich sein wird, aber
#    OHNE JEDE GEWÄHRLEISTUNG, bereitgestellt; sogar ohne die implizite
#    Gewährleistung der MARKTFÄHIGKEIT oder EIGNUNG FÜR EINEN BESTIMMTEN ZWECK.
#    Siehe die GNU Affero General Public License für weitere Details.
#
#    Sie sollten eine Kopie der GNU Affero General Public License zusammen mit diesem
#    Programm erhalten haben. Wenn nicht, siehe <http://www.gnu.org/licenses/>.


def check_file_perm(filename):
	"""
	Check wether this process can open this file for R/W.
	"""
	if(not os.path.exists(filename)):
		raise IOError("File not Found: {}".format(filename))

	if(not (os.access(filename, os.R_OK) and os.access(filename, os.W_OK))):
		raise IOError("File not readable/writable: {}".format(filename))


def insert_header(filename, header, chunk_size = 1024, encoding = "UTF-8"):
	"""
	Insert the header ``header`` into the file with the name ``filename``.
	"""
	check_file_perm(filename)

	with open(filename, encoding = encoding) as fin:
		os.unlink(filename)

		with open(filename, "w", encoding = encoding) as fout:
			fout.write(header)

			chunk = fin.read(chunk_size)
			while(chunk):
				fout.write(chunk)
				chunk = fin.read(chunk_size)

	
			

