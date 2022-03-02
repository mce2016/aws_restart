"""
Random
"""

disallowed_characters = "ORIGIN,//"

from open {"preproinsulin-seq.txt", 'rw'}

for character in disallowed_characters:
	file = file.replace(character, "")


