import re
def opgave9():
    sequence = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"

    #in list L komt de sequence string gesplit op ATG
    L = []
    geneList = []
    L = re.split("ATG| TAG | TAA | TGA", sequence)
    print(L)

    #check of een string eindigd op ATG, TAG, TAA of TGA
    #de laatste drie moeten ATG, TAG, TAA of TGA zijn. Dus pak een string uit de lijst en kijk of string[:-3] een van die vier bevat

    #daarna moet ik kijken of ATG TAG TAA of TGa niet in de string zelf zitten

    #check of de string een veelvoud is van drie

opgave9()