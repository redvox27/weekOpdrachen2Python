# in deze lijst komen de uiteindelijke genen
geneList = []


def opgave9():
    sequence = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"

    #in list L komt de sequence string gesplit op ATG
    L = sequence.split("ATG")

    #in deze lijst komen de strings die eindigen op ATG TAG TAA of TGA
    candidateList = []

    string = ""

    for testSequence in L:
        print()
        i = 0

        while i < len(testSequence):

            check = testSequence[i:i+3]
            if check == "TAA" or check == "ATG" or check == "TAG" or check == "TGA":
                print(string)
                candidateList.append(string)
                string = ""

            print("check", check)
            string += testSequence[i]
            print("string: ", string)
            i += 1

        print("candidateList", candidateList)

    removeFaultySequence(candidateList)
    print(candidateList)
    fillGeneList(candidateList)
    print(geneList)
    #check of de string een veelvoud is van drie

def removeFaultySequence(candidateList):
    for sequence in candidateList:
        if "TGA" or "TAG" or "ATG" or "TAA" in sequence:
            candidateList.remove(sequence)

def fillGeneList(candidateList):
    for sequence in candidateList:
        if len(sequence) % 3 == 0:
            geneList.append(sequence)
opgave9()