###########################################################################################################
# namen auteurs: Thijs Ermens, Christiaan Posthuma en Jasper Versantvoort
# datum 13 oktober 2020
# functie: een pipline die met behulp van een MSA opzoek gaat naar vergelijkbare eiwitten
# Er wordt gebruikt gemaatk van MAFFT, HMMbuild en HMMsearch.
###########################################################################################################
import os.path
import subprocess


class pipeline():
    def __init__(self, input_file_name):
        print("created new instance of pipeline")
        self.fasta_to_msa = input_file_name

    def clustalO(self, output_file):
        """ runt clustalO via de commandline van linux
        :param output_file: een msa file van clustalO
        :return:
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
        """ runt een mafft via de commandline in linux
        :param output_file: msa file van mafft
        :return:
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
        """ runt hmmbuild in commandline van linux
        :param input_file: een msa file
        :param output_file: een hmm file van de msa
        :return:
        """
        # Checks if file exists
        if os.path.isfile("{}".format(output_file)):
            print("hmmer pass")
            pass
        # If not, command will run on the command line
        else:
            print("bezig met hmm")
            cmd = "hmmbuild {} {}".format(output_file, input_file)
            print(cmd)
            e = subprocess.check_call(cmd, shell=True)
        return

    def hmmsearch(self, outputfile, inputfile, database):
        """ runt hmm search uit op commandline van linux
        :param outputfile: file die als output de gevonden sequenties en een msa geeft
        :param inputfile: de hmm van de hmmbuild
        :param database: de gekozen database
        :return:
        """
        if os.path.isfile("{}".format(outputfile)):
            print("hmm search pass")
            pass
        else:
            print("bezig met hmm search")
            # Usage: hmmsearch -A <output> <hmmfile> <seqdb>
            cmd = "hmmsearch -A {} {}.hmm {}".format(outputfile, inputfile, database)
            print(cmd)
            e = subprocess.check_call(cmd, shell=True)

    def hmmsearchipa(self, outputfile, inputfile):
        """via de url van de webpagina van hmmer een hmmsearch uitvoert via commandline in linux
        :param outputfile: file die je eruit wilt hebben
        :param inputfile: inputfile van hmmbuild
        :return: html met gevonden resultaten en hmm
        """
        if os.path.isfile("{}.html".format(outputfile)):
            print("hmmipa search pass")
            pass
        else:
            print("bezig hmmipa search")
            cmd = \
                "curl -L -H 'Expect:' -H 'text' -F taxFilterType=search -F tax_included=2759  -F seqdb=uniprotrefprot" \
                " -F seq='<{}' https://www.ebi.ac.uk/Tools/hmmer/search/hmmsearch > {}".format(
                    inputfile, outputfile)
            print(cmd)
            e = subprocess.check_call(cmd, shell=True)


# mogelijkheid om stapgeweis via de hmmsearchipa te werken
i = 0
fasta_to_msa = "eiwittenEukaryoten.txt"
pipeline = pipeline(fasta_to_msa)  # create a new object, with the fasta inside
pipeline.mafft("mafft_run" + str(i) + "_data_output_mafft")
pipeline.hmmer(input_file="mafft_run" + str(i) + "_data_output_mafft",
               output_file="hmm_run" + str(i) + "_hmm.hmm")
pipeline.hmmsearchipa(outputfile="testipa2.html",
                      inputfile="hmm_run" + str(i) + "_hmm.hmm")
i += 1
pipeline.hmmer(input_file="msasearch1.hmm", output_file="hmm_run" + str(i) + "_hmm.hmm")
pipeline.hmmsearchipa(outputfile="testipa2.2.html", inputfile="hmm_run" + str(i) + "_hmm.hmm")

# mogelijkheid om via de hmmsearch een loop uit te voeren.
# for i in range(3):
#     if i == 0:
#         pipeline.hmmsearch(outputfile="hmm_search" + str(i) + "_sto",
#                            inputfile="hmm_run" + str(i) + "_hmm",
#                            database="/home/jversantvoort/Programs/nr/nr")
#     else:
#         pipeline.hmmer(input_file="hmm_search" + str(i - 1) + "_sto",
#                        output_file="hmm_run" + str(i) + "_hmm")
#         pipeline.hmmsearch(outputfile="hmm_search" + str(i) + "_sto",
#                            inputfile="hmm_run" + str(i) + "_hmm",
#                            database="/home/jversantvoort/Programs/nr/nr")
