licor -- Disclaimer Helper
**************************

licor (pronounciated liquor) is a little script that allows
programmers to add copyright/license/warranty disclaimers to
all their files easily.

.. contents::


Usage
=====

Usage::

       licor list-db [<path>] [options]
       licor list-all [<path>] [options]
       licor list-path [<path>] [options]
       licor list-templates [options]
       licor print-templ <format> [options]
       licor insert-header <format> [<path>] [options]

Options::

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


License
=======

licor is licensed under the GNU AGPLv3.

Contributing
============

Just send a pull request. Or an email.
