"""""
*author - Ritesh KT
*date - 31-07-2021
*time - 09:00 AM
*title - Read and Write data in TXT File
"""""

class TxtFileIo:
    def writeDataIntoFile(self):
        write_into_file = open('python.txt', 'w')
        write_into_file.write("I love java \nI love Angular")
        write_into_file.close()

    def readDataFromFile(self):
        read_from_file = open('python.txt', 'r')
        data = read_from_file.read()
        print(data)
        read_from_file.close()

txtFileIo = TxtFileIo()
txtFileIo.writeDataIntoFile()
txtFileIo.readDataFromFile()
