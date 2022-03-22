import sys


def find_alphabet(word):
    result = [-1 for i in range(26)]
    for i in range(len(word) - 1):
        if (result[ord(word[i]) - ord('a')] == -1):
            result[ord(word[i]) - ord('a')] = i
        else:
            continue
    return result


if __name__ == '__main__':
    word = sys.stdin.readline()
    result = find_alphabet(word)

    for i in range(26):
        print(result[i], end = " ")
