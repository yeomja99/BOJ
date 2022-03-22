import sys


def lastarr(sentence):
    result = list()
    for i in range(len(sentence)):
        result.append(sentence[-i:])

    result.sort()
    return result
if __name__ == '__main__':
    sentence = sys.stdin.readline()
    sentence = sentence[:-1]
    result = lastarr(sentence)

    for i in result:
        print(i)

