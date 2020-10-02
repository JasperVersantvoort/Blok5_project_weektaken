import os.path
import subprocess
from sys import argv
from tkinter.filedialog import askopenfilename
from tkinter import filedialog


class pipeline():

    def __init__(self, input_file_name):
        print("created new instance of pipeline")
        self.input_file = input_file_name

    def clustalO(self,output_file):
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

fasta_to_msa  = filedialog.askopenfilename()
print(fasta_to_msa)
MSA_to_HMM = "MSA_{}".format("")
output_HMM = "HMM_{}".format("")

# to run on command line:
# fasta_to_msa  = argv[1]
# MSA_to_HMM = = argv[2]
# output_HMM = = argv[3]

pipeline = pipeline(fasta_to_msa)
pipeline.clustalO(output_file=MSA_to_HMM)
pipeline.hmmer(output_HMM)


