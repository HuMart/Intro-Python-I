"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
import os
print(os.getcwd())

file = open("foo.txt", "r")
print(file.readlines())

file.close()
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
file2 = open("bar.txt", "w")

file2.write("gsfvbvjdnvnd\n")
file2.write("123456789\n")
file2.write("jfhfhjnjfnbjnf\n")

file2.close()

file2 = open("bar.txt", "r")
print(file2.readlines())

file2.close()