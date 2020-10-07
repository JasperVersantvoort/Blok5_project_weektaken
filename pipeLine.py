import os.path
import subprocess
from datetime import date
from sys import argv



class pipeline():

    def __init__(self, input_file_name):
        print("created new instance of pipeline")
        self.fasta_to_msa = input_file_name

    def clustalO(self, output_file):
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
            cmd = "clustalo -i {} -o {}".format(self.fasta_to_msa, output_file)
            e = subprocess.check_call(cmd, shell=True)
        return

    def mafft(self, output_file):
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
            print("mafft pass")
            pass
        # If not, command will run on the command line
        else:
            cmd = "mafft --auto {} > {}".format(self.fasta_to_msa, output_file)
            e = subprocess.check_call(cmd, shell=True)
            print(cmd)

        return

    def hmmer(self, input_file, output_file):
        """Runs Hmmr on linux command line

        Input:
        MSA file that

        Return:
        hmmr retuns a file with the hmm profile, this van be found in the current path
        unless otherwise specified
        """
        # Checks if file exists
        if os.path.isfile("{}.hmm".format(output_file)):
            print("hmmer pass")
            pass
        # If not, command will run on the command line
        else:
            print("bezig met hmm")
            cmd = "hmmbuild {}.hmm {}".format(output_file, input_file)
            print(cmd)
            e = subprocess.check_call(cmd, shell=True)
        return


for i in range(3):
    fasta_to_msa = "/home/jversantvoort/PycharmProjects/Blok5_project_weektaken/venv/eiwittenEukaryoten.txt"
    pipeline = pipeline(fasta_to_msa)  # create a new object, with the fasta inside
    pipeline.mafft("/home/jversantvoort/PycharmProjects/Blok5_project_weektaken/venv/mafft_run" + str(i) + "_data_output_mafft")
    pipeline.hmmer(input_file="/home/jversantvoort/PycharmProjects/Blok5_project_weektaken/venv/mafft_run" + str(i) + "_data_output_mafft",
                   output_file="/home/jversantvoort/PycharmProjects/Blok5_project_weektaken/venv/hmm_run" + str(i) + "_hmm")


