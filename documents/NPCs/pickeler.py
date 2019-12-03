""" A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import sys
import pickle
class pklr:

    def pkl (self,data,file_name):
        """A method which pickles the inputted data and saves it into the file"""
        #create the file if it does not exist
        try:
            file = open(file_name,"x")
            file.close()
        except FileExistsError:
            pass

        #pickle the resulting counter and save as a file
        writeFile = open(file_name,"wb")
        pickle.dump(data,writeFile)
        writeFile.close()

    def unpkl (self,file_name):
        """A method that unpickles the data stored in a file"""
        try :
            readFile = open(file_name, "rb")
            data = pickle.load(readFile)
            readFile.close()
            return data
        except EOFError:
            return None

if __name__ == '__main__':
    #sys.argv
    pickler = pklr()
    #pickle the dialogue lines
    pickler.pkle(sys.argv[1],sys.argv[2])
    #pickel the key codes
    pickler.pkle(sys.argv[3],sys.argv[4])
