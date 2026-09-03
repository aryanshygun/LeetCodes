from ast import List


class Solution:
    def twoEditWords(self, queries: list[str], dictionary: list[str]) -> List[str]:
        xlist = []
        for query in queries:
            for entry in dictionary:
                count = 0
                for k in range(len(query)):
                    if query[k] != entry[k]:
                        count += 1

                if count <= 2:
                    xlist.append(query)
                    break
        return xlist
