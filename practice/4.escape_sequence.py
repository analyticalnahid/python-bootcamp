#\n: A newline character, which represents a line break.

message = "Hello,\nWorld!"
print(message)  # Outputs "Hello,\nWorld!" on two separate lines



#\t: A tab character, which represents a horizontal tab.

message = "Hello,\tWorld!"
print(message)  # Outputs "Hello,   World!"



# \\: A backslash character, which represents a single backslash.

message = "Hello,\\World!"
print(message)  # Outputs "Hello,\World!"



# \': A single quote character, which represents a single quote within a string that is delimited by single quotes.

message = 'Hello,\'World!\''
print(message)  # Outputs "Hello,'World!'"



# \": A double quote character, which represents a double quote within a string that is delimited by double quotes.

message = "Hello,\"World!\""
print(message)  # Outputs "Hello,"World!""



#\r: A carriage return character, which represents a line break that moves the cursor to the beginning of the line.

message = "Hello,\rWorld!"
print(message)  # Outputs "World!Hello,"



#\a: A bell character, which causes the console to emit a beep sound.

message = "Hello,\aWorld!"
print(message)  # Outputs "Hello,World!" and causes the console to emit a beep sound




#\b: A backspace character, which moves the cursor one character to the left.

message = "Hello,\bWorld!"
print(message)  # Outputs "Hello,World!" and removes the character before the "W"




#\f: A form feed character, which represents a page break.

message = "Hello,\fWorld!"
print(message)  # Outputs "Hello,World!" and moves the cursor to the top of the next page




#\o: An octal escape sequence, which represents a character with an ASCII value specified by an octal number.

message = "Hello,\141World!"
print(message)  # Outputs "Hello,aWorld!"




#\x: A hexadecimal escape sequence, which represents a character with an ASCII value specified by a hexadecimal number.


message = "Hello,\x61World!"
print(message)  # Outputs "Hello,aWorld!"
Footer
