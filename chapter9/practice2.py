#open a file called report.txt in write mode.
file=open("report.txt","w")
file=open("report.txt","a")
file.write("this the first append line the main difference b/w write and append is write overwrites the text whereas append just adds the text.\n")
file.write("this is the first line of the report.\n")
file.write("this is the second line of the report.\n")
file.close()