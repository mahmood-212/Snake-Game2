import textract
import docx2txt

# file = open("c:/Users/MOHMOOD/Desktop/my_file.txt")
# constant = file.read()
# print(constant)
# file.close()

# with open("new_file", mode="r") as file:
#     # file.write("\n6")
#     s1 = file.read()
#     print(s1)
#     file.close()


with open("./new_file", "r") as file:
    file_1 = file.read()
    print(file_1)

with open("../m1.txt") as mm:
    m3 = mm.read()
    print(m3)

# with docx2txt.process().open(docx2txt. process("c:/Users/MOHMOOD/Desktop/important link.docx", "r")) as file_2:
#     m4 = file_2.read()
#     print(m4)
# Here how to open word file by using "docx2txt" than use "docx2txt.process()" :
my_text = docx2txt.process("c:/Users/MOHMOOD/Desktop/important link.docx")
print(my_text)

# with open("d:/monthGoals.txt", "r") as files:
#     m5 = files.read()
#     print(m5)

with open("../../../../monthGoals.txt") as files:
    m5 = files.read()
    print(m5)