# Copyright (c) 2017 Daniel Knüttel                                           #
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



from .main import (list_this_path, list_all, list_db, 
		print_uncommented_line_based, 
		print_uncommented_block_based, 
		print_template_options, insert_templates_all)
import docopt, datetime, sys

usage = '''\

Insert license/copyright/warranty disclaimer to source files.

Usage:
       licor list-db [<path>] [options]
       licor list-all [<path>] [options]
       licor list-path [<path>] [options]
       licor list-templates [options]
       licor print-templ <format> [options]
       licor insert-header <format> [<path>] [options]

Options:
       --comment-start=<comment-start>                 Comment start token to use [default: //]
       --comment-stop=<comment-stop>                   Comment stop token to use [default: */]
       --border=<border>                               Border character for some fancy stuff [default: *]
       -f --fancy                                      Use more fancy comments 
       --after-comment=<after-comment>                 A string to seperate border and content (defaults to one blank)
       -c --confirm                                    Wait for user confirmation before modifying files
       --format=<format>                               Use a special comment format [default: block]
       --license=<license>                             Use this license template [default: GPLv3]
       --single-file                                   Use single-file templates
       --copyright                                     Use templates containing copyright information
       -a <author> --author=<author>                   Set the author (required for --copyright)
       -p <project> --project=<project>                Set the project (required unless --single-file is specified)
       -e <ending> --file-ending=<ending>              Search for files ending with this ending [default: c]
       -i --ignore-db                                  Ignore the database of processed files
       --ignore-paths=<paths>                          Ignore all paths with one of `<paths>` in it (comma-seperated) [default: .git]
       --pad-to=<pad-to>                               Pad comment blocks to this width [default: 0]
'''

if( __name__ == "__main__"):
	args = docopt.docopt(usage)

	if(args["list-db"]):
		path = args["<path>"]
		if(not path):
			path = "."
		try:
			list_db(path)
		except Exception as e:
			print(e)
			sys.exit(1)

	if(args["list-path"]):
		path = args["<path>"]
		if(not path):
			path = "."
		ending = args["--file-ending"]
		ignore_db = args["--ignore-db"]

		list_this_path(path, ending, ignore_db = ignore_db)

	if(args["list-all"]):
		path = args["<path>"]
		if(not path):
			path = "."
		ending = args["--file-ending"]
		ignore_paths = args["--ignore-paths"].split(",")
		ignore_db = args["--ignore-db"]

		list_all(path, ending, ignore_paths, ignore_db = ignore_db)

	if(args["print-templ"]):
		form = args["<format>"]
		license_name = args["--license"]
		modifiers = []
		if(args["--single-file"]):
			modifiers.append("single-file")
		if(args["--copyright"]):
			modifiers.append("copyright")

		data = {}
		if(args["--author"]):
			data["author"] = args["--author"]
		if(args["--project"]):
			data["project"] = args["--project"]
		data["year"] = str(datetime.datetime.now().year)

		after_comment = " "
		if(args["--after-comment"]):
			after_comment = args["--after-comment"]

		try:
			pad_to = int(args["--pad-to"])
		except:
			print("Failed to convert {} to int".format(args["--pad-to"]))
			sys.exit(1)

		if(form == "line"):
			print_uncommented_line_based(license_name, modifiers, data, args["--comment-start"],
					fancy = args["--fancy"], after_comment = after_comment,
					pad_to = pad_to)
		elif(form == "block"):
			method = args["--format"]
			if(not method):
				method = "line"

			print_uncommented_block_based(license_name, modifiers, data,
					args["--comment-start"], args["--comment-stop"],
					border = args["--border"],
					fancy = args["--fancy"], after_comment = after_comment,
					method = method,  pad_to = pad_to)
		else:
			print("Unknown format ({}). Use line or block.".format(form))
		
	if(args["list-templates"]):
		print_template_options()

	if(args["insert-header"]):
		form = args["<format>"]
		license_name = args["--license"]
		modifiers = []
		if(args["--single-file"]):
			modifiers.append("single-file")
		if(args["--copyright"]):
			modifiers.append("copyright")

		data = {}
		if(args["--author"]):
			data["author"] = args["--author"]
		if(args["--project"]):
			data["project"] = args["--project"]
		data["year"] = str(datetime.datetime.now().year)

		after_comment = " "
		if(args["--after-comment"]):
			after_comment = args["--after-comment"]

		try:
			pad_to = int(args["--pad-to"])
		except:
			print("Failed to convert {} to int".format(args["--pad-to"]))
			sys.exit(1)
		method = args["--format"]
		if(not method):
			method = "line"

		path = args["<path>"]
		if(not path):
			path = "."
		ignore_paths = args["--ignore-paths"].split(",")
		ignore_db = args["--ignore-db"]
		insert_templates_all(path, args["--file-ending"], ignore_paths, license_name,
				modifiers, data, args["--comment-start"], args["--comment-stop"],
				form, method = method, border = args["--border"], fancy = args["--fancy"],
				after_comment = after_comment, pad_to = pad_to, ignore_db = args["--ignore-db"],
				confirm = args["--confirm"])
