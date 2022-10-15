# Alex Zaremba
# October 11th, 2022




file_name = input('Please enter name of the file: ') # Ask user for file name
out_file = file_name + ".html" # Convert file to html

body_h1 = input('Please enter character\'s name: ') # Request name of character
body_h1 = "<h1>" + body_h1 + "</h1>\n"

body_h2 = input('Please enter the actor\'s name: ') # Request name of actor
body_h2 = "<h2>Played by " + body_h2 + "</h2>\n"

body_description = input('Please enter a description of the character: ') # Request a description of the character
body_description = "<p>" + body_description + "</p>\n"

body_img = input('Please enter location of an image file of the character, either on your PC or through a url: ') # Request location of character image
body_img = '<img src="' + body_img + '" alt="' + file_name + '">\n'

combined_body = file_name + body_h1 + body_h2 + body_description + body_img # Merge user inputs into one variable

# Define template pages

page_head = ()
page_footer = ()

# Read template files and put into variables

f = open('assets/page-head.txt', "r")
combined_head = ''.join(f.readlines())
f.close()
f= open('assets/page-footer.txt', "r")
combined_footer = '' .join(f.readlines())
f.close()

# Write HTML file

f =open(out_file, "w")
f.write(combined_head + combined_body + combined_footer)
f.close()
print ("Created {}".format(out_file))