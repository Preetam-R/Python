#while writing the files we have two mwthod to write 
#first method is that we can open the file in w mode Which over writes the entire file/data
#second is that by opening the fine in a mode which is append mode which adds the data at the last of the existing data.

#by using append mode

f = open("files.txt","a")
f.write(" Hello again i am writing this data by append method")
f.close()