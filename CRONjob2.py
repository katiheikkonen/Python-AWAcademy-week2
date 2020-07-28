from datetime import datetime
myFile = open('CRONjobappend.txt', 'a')
myFile.write('\nAccessed on ' + str(datetime.now()))
myFile.close()
