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

import pkg_resources, json
from itertools import permutations
from string import Template

class TemplateException(Exception): 
	pass

def get_resource_string(name):
	"""
	Return the resource string with the given name UTF-8 encoded.
	"""
	return pkg_resources.resource_string(__name__,"templates/" + name).decode("UTF-8")


def get_license_template(name, modifiers = []):
	"""
	Return a ``dict`` containing all necessary information for 
	filling a license template::

		{
			"name": <template-name>,
			"keywords": ["author", "date", ...],
			"text": <template string>
		}

	``modifiers`` is a list specifying the template. 
	A typical call might be::

		get_license_template("AGPL", modifiers = ["single-file"])
	"""

	templates_avail = json.loads(get_resource_string("licenses_avail.json"))

	if( not name in templates_avail):
		raise TemplateException("Unknown license: {}".format(name))

	unsupported = [mod for mod in modifiers if not mod in templates_avail[name]["modifiers"]]
	if(unsupported):
		raise TemplateException("Unknown modifiers: {}. Supported are: {}".format(
					",".join(unsupported), ",".join(templates_avail[name]["modifiers"])))
	
	for perm in permutations(modifiers):
		mods = ".".join(perm)
		if(mods):
			meta_name =  ".".join((name, mods, "meta"))
			data_name = ".".join((name, mods, "tx"))
		else:
			meta_name = ".".join((name, "meta"))
			data_name = ".".join((name, "tx"))
		try:
			meta = json.loads(get_resource_string(meta_name))
		except:
			continue

		data = get_resource_string(data_name)

		meta.update({"text": data})
		return meta

	raise TemplateException("Database licenses_avail.json is desynced. Unable to locate resource.")

def get_license_meta(name, modifiers = []):
	"""
	Return a ``dict`` containing all necessary information for 
	filling a license template::

		{
			"name": <template-name>,
			"keywords": ["author", "date", ...]
		}

	``modifiers`` is a list specifying the template. 
	A typical call might be::

		get_license_meta("AGPL", modifiers = ["single-file"])
	"""

	templates_avail = json.loads(get_resource_string("licenses_avail.json"))

	if( not name in templates_avail):
		raise TemplateException("Unknown license: {}".format(name))

	unsupported = [mod for mod in modifiers if not mod in templates_avail[name]["modifiers"]]
	if(unsupported):
		raise TemplateException("Unknown modifiers: {}. Supported are: {}".format(
					",".join(unsupported), ",".join(templates_avail[name]["modifiers"])))
	
	for perm in permutations(modifiers):
		mods = ".".join(perm)
		if(mods):
			meta_name =  ".".join((name, mods, "meta"))
		else:
			meta_name = ".".join((name, "meta"))
		try:
			meta = json.loads(get_resource_string(meta_name))
		except:
			continue

		return meta

	raise TemplateException("Database licenses_avail.json is desynced. Unable to locate resource.")


def format_license_template(name, data, modifiers = []):
	"""
	Return a formatted version of the license Template.
	This text is ready to be uncommented an placed into a source file.
	"""
	template = get_license_template(name, modifiers)

	missing = [k for k in template["keywords"] if not k in data]
	if(missing):
		raise TemplateException("missing keywords: {}".format(",".join(missing)))
	
	return Template(template["text"]).substitute(data)

def get_templates_available():
	"""
	Return a ``dict`` containing information about the available templates.
	"""
	return json.loads(get_resource_string("licenses_avail.json"))
