# f = open('./demo.txt','r')       #open('filename','mode')
# print(f.read())   




# f = open('./demo.txt','r')
# print(f.readline())                #readline() --> to read first line



# f = open('./demo.txt','r')
# print(f.readline()[0])             #to assess the characters through index 



# f = open('./demo.txt','r')
# print(f.readlines()[1])



# f = open('./demo.txt','r')
# for x in f:                   #printing each line
#     print(x)



# f.close()           #closing the file




# f = open('./new.txt','w')             #to write in file with mode 'w'
# f.write("\nHi this is new file.")
# f.write('\nI am writting in this file using the .write file handling code.')
# f.close()




# f = open('./new.txt','a')             #to append in file with mode 'a'
# f.write("\nHi this is new file.")
# f.write('\nI am appending in this file using the .write file handling code.')
# f.close()



# import os

# os.remove()       # os.remove("path of file name")
# os.rmdir()        # os.rmdir("folder name") --> only empty folders can be deleted





# import os

# if os.path.exists("demo.txt"):
#     print("The file exists.")
# else:
#     print("File doesn't exists")
