# Defines variables
tabby_cat = "\tI'm tabbed in." # Defines the string tabbed in
persian_cat = "I'm split\non a line." # Defines the string on 2 lines using \n escape sequence
backslash_cat = "I'm \\ a \\ cat." # Defines the string escaping backslashes

# Defines variable and writes string (list) on multiple lines
# """ allows string to run onto multiple lines
# \t* tabs line in
# NONE OF THIS IS PRINTED UNTIL LINE 22
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass 
"""
# "Catnip\n\t* Grass" indents Catnip, the \n escapes the line to the next one and 
# t* Grass writes on the new line

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat