class GeneSearcher():
    sequence = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"
    #hierin komen alle indexes waar ATG gevonden wordt
    indexList = []
    #hierin komen alle strings die beginnen met ATG
    beginATGList = []
    testList = []
    #hierin komen de strings die na ATG komen en voor ATG TAG TAA of TGA
    candidateList = []
    #hierin komen de uiteindelijke genen in
    geneList = []

    L = []


    #deze methode zoekt naar de indexes waar ATG in voorkomen
    def fillIndexList(self):
        for index in range(0, len(self.sequence)):
            if self.sequence[index: index + 3] == "ATG":
                self.indexList.append(index)

    #Deze methode kijkt tussen de indexes voor sequences die beginnen met atg
    def fillBeginATGList(self):
        i = 0
        while i < len(self.indexList):
            if (i == len(self.indexList) - 1):
                gene = self.sequence[self.indexList[i]:]
                self.beginATGList.append(gene)
            else:
                gene = self.sequence[self.indexList[i]: self.indexList[i + 1]]
                self.beginATGList.append(gene)


            i += 1
    #deze methode schrapt de "ATG" aan het begin van de sequences
    def fillCandidateList(self):
        for sequence in self.beginATGList:
            sequence = sequence[3:]
            if (len(sequence) > 3):
                self.candidateList.append(sequence)

    #deze methode zoekt naar de woorden TAA, ATG, TAG en TGA. als de woorden zijn govonden, stop met loopen en append naar geneList
    def fillGeneList(self):

        for sequence in self.candidateList:
            i = 0
            string = ""

            while i < len(sequence) - 3:
                check = sequence[i:i + 3]
                if check == "TAA" or check == "ATG" or check == "TAG" or check == "TGA":
                    self.geneList.append(string)
                    break

                string += sequence[i]
                i += 1

    #kijkt of de sequences deelbaar zijn door 3
    def cleanGeneList(self):
        for sequence in self.geneList:
            if not len(sequence) % 3 == 0 :
                self.geneList.remove(sequence)

    def main(self):
        self.fillIndexList()
        self.fillBeginATGList()
        self.fillCandidateList()
        self.fillGeneList()
        self.cleanGeneList()
        print(self.geneList)


g = GeneSearcher()
g.main()