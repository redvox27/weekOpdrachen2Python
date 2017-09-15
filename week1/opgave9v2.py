class GeneSearcher():
    sequence = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"
    indexList = []
    #hierin komen alle strings die beginnen met ATG
    beginATGList = []
    testList = []
    candidateList = []

    L = []

    def fillIndexList(self):
        for index in range(0, len(self.sequence)):
            if self.sequence[index: index + 3] == "ATG":
                print(index)
                self.indexList.append(index)

    def fillBeginATGList(self):
        i = 0
        while i < len(self.indexList):
            if (i == len(self.indexList) - 1):
                gene = self.sequence[self.indexList[i]:]
                print(gene)
            else:
                gene = self.sequence[self.indexList[i]: self.indexList[i + 1]]
                print(gene)


            i += 1
g = GeneSearcher()
g.fillIndexList()
g.fillBeginATGList()
