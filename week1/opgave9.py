# in deze lijst komen de uiteindelijke genen
geneList = []


def opgave9():
    sequence = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"

    # CATGTCATGCG
    #in list L komt de sequence string gesplit op ATG
    L = sequence.split("ATG")
    print(L)

    #in deze lijst komen de strings die eindigen op ATG TAG TAA of TGA
    candidateList = []

    string = ""

    for testSequence in L:
        print()
        i = 0

        while i < len(testSequence):

            check = testSequence[i:i+3]
            if check == "TAA" or check == "ATG" or check == "TAG" or check == "TGA":
                candidateList.append(string)
                string = ""

            string += testSequence[i]
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
