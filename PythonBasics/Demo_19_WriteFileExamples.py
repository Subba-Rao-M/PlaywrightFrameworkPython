#To open the file in another way
#file = open('demofile.txt')
#file.close()

# Add parameters r - only read mode, w - for write mode
## add a program to read the file lines, reverse it and write the reversed data to file
#below line opens and closes the file automatically
with open('demofile.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('demofile.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)


#With statement is used for exception handling where open, edit saving and closing file is involved