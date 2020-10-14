# to use this create a file named input.txt, in it add the words in
# any format(sentences or word in each line). You can check if the given
# input by the user is present or not in the file.
class Node:
    def __init__(self):
        self.array = [None] * 26
        self.eow = False


class Trie:
    def __init__(self):
        self.root = Node()

    def createNode(self):
        return Node()

    def getIndex(self, a):
        """this is used to give the index of an alphabet with the index os a as 0,b as 1..."""
        return ord(a) - ord('a')

    def insert(self, a):
        """this is used to insert into a trie, a word is given as input"""
        word = list(a)
        r = self.root
        for level in range(len(word)):
            if r.array[self.getIndex(word[level])] is None:
                r.array[self.getIndex(word[level])] = self.createNode()
            r = r.array[self.getIndex(word[level])]
        r.eow = True

    def search(self, a):
        """word is input,returns a boolean value"""
        word = list(a)
        r = self.root
        for level in range(len(word)):
            if r.array[self.getIndex(word[level])] is None:
                return False
            r = r.array[self.getIndex(word[level])]
        if r.eow is True:
            return True
        return False


def main():
    t = Trie()
    f = open("input.txt", "r")
    for line in f.readlines():
        ls = list(line.split(" "))
        ls[-1] = ls[-1].strip()
        for i in range(len(ls)):
            t.insert(ls[i])

    n1 = int(input("Enter the number of words:"))
    for i in range(n1):
        key = input("Enter the word:")
        print(t.search(key))


if __name__ == '__main__':
    main()
