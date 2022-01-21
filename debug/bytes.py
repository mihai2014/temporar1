#  Byte objects are sequence of Bytes, whereas Strings are sequence of characters.
#  Byte objects are in machine readable form internally, Strings are only in human readable form.
#  Since Byte objects are machine readable, they can be directly stored on the disk. Whereas, Strings need encoding before which they can be stored on disk.

#        -> encode:   PNG, JPEG, MP3, WAV, ASCII, UTF-8
#string          byte
#        <- decode

import io

file = io.BytesIO(b'this is a byte string')
stream = file.read()
print(stream)

# Text I/O (str obj)
#f1 = open("myfile.txt", "r", encoding="utf-8")
#f2 = io.StringIO("some initial text data")

# Binary I/O (bytes obj)
#f3 = open("myfile.jpg", "rb")
#f4 = io.BytesIO(b"some initial binary data: \x00\x01")


string_stream = io.StringIO("Hello from Journaldev\nHow are you?")
 
# Print old content of buffer
print(f'Initially, buffer: {string_stream.getvalue()}')
 
# Write to the StringIO buffer
string_stream.write('This will overwrite the old content of the buffer if the length of this string exceeds the old content')
 
print(f'Finally, buffer: {string_stream.getvalue()}')
 
# Close the buffer
string_stream.close()


input = io.StringIO('This goes into the read buffer.')
print(input.read())


#----------------------------------------------

# Python code to demonstrate String encoding
 
# initialising a String
a = 'GeeksforGeeks'
 
# initialising a byte object
c = b'GeeksforGeeks'
 
# using encode() to encode the String
# encoded version of a is stored in d
# using ASCII mapping
d = a.encode('ASCII')
 
# checking if a is converted to bytes or not
if (d==c):
    print ("Encoding successful")
else : print ("Encoding Unsuccessful")



# Python code to demonstrate Byte Decoding

# initialising a String
a = 'GeeksforGeeks'

# initialising a byte object
c = b'GeeksforGeeks'

# using decode() to decode the Byte object
# decoded version of c is stored in d
# using ASCII mapping
d = c.decode('ASCII')

# checking if c is converted to String or not
if (d==a):
    print ("Decoding successful")
else : print ("Decoding Unsuccessful")
