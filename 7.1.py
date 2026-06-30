# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("AI God failed to find a file my that name! DO BETTER!")
fh = fh.read()
fh = fh.rstrip()
print(fh.upper())
