import sys


def cnt_alphabet(word):
    result = [0 for i in range(26)]
    for i in range(len(word) - 1):
        index = (ord(word[i]) - ord('a'))
        result[index] += 1
    return result

if __name__ == '__main__':
    word = sys.stdin.readline()
    result = cnt_alphabet(word)
    for i in range(len(result)):
        print(result[i], end = " ")
