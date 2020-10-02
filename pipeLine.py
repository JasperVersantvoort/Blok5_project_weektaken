import os.path
import subprocess
from sys import argv
from tkinter.filedialog import askopenfilename
from tkinter import filedialog


class pipeline():

    def __init__(self, input_file_name):
        print("created new instance of pipeline")
        self.input_file = input_file_name

    def clustalO(self,output_file_name):
        """Runs ClustalO on linux command line

        Input:
        input_file - str, name of fasta file to create MSA
        output_file - str,name output of ClustalO

        Return:
        ClustalO returns a file, the file can be found in the current path
        unless otherwise specified
        """
        # Checks id file exists
        if os.path.isfile(output_file):
            pass
        # If not, command will run on the command line
        else:
            cmd = "clustalo -i {} -o {}".format(self.input_file, output_file)
            e = subprocess.check_call(cmd, shell=True)
        return


    def hmmer(output_bestand):
        """Runs Hmmr on linux command line

        Input:
        output_file

        Return:
        hmmr retuns a file with the hmm profile, this van be found in the current path
        unless otherwise specified
        """
        # Checks if file exists
        if os.path.isfile("{}.hmm".format(output_bestand)):
            pass
        # If not, command will run on the command line
        else:
            cmd = "hmmbuild {}.hmm {}".format(output_bestand, output_bestand)
            e = subprocess.check_call(cmd, shell=True)
        return


# to run in the IDE:

input_file_name  = filedialog.askopenfilename()
output_file_name = filedialog.askopenfilename()

# to run on command line:
# input_file = argv[1]
# output_file = argv[2]

pipeline = pipeline(input_file_name)
pipeline.clustalO(output_file_name=output_file_name)
pipeline.hmmer(output_file_name)


