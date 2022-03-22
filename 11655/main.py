import sys


def ROT13(word):
    for i in range(len(word) - 1):
        if (word[i] >= 'A' and word[i] <= 'Z'):
            s = ord(word[i]) + 13
            if (s > 90):
                print(chr(s - 90 + ord('A') - 1), end="")
            else:
                print(chr(s), end="")
        elif (word[i] >= 'a' and word[i] <= 'z'):
            s = ord(word[i]) + 13
            if (s > 122):
                print(chr(s - 122 + ord('a') - 1), end="")
            else:
                print(chr(s), end="")
        else:
            print(word[i], end="")


if __name__ == '__main__':
    word = sys.stdin.readline()
    ROT13(word)
