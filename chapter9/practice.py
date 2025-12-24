#write a pprogram to read a text from a given file certificte.txt and find whether it contains the word live.

file=open("certificate.txt","r")
data=file.read()
data=data.lower()
if"live"in data:
    print("the word live is present in the file.")
else:
    print("the word live is not present is the file.")
