import sys
def reverse(sentence):
    temp_word = list()
    i = 0
    while(i < len(sentence)):
        if (sentence[i] == '<'):
            if(len(temp_word)>0):
                for w in range(len(temp_word)- 1, -1, -1):
                    print(temp_word[w], end = "")
                temp_word.clear()
            while (sentence[i] != '>'):
                print(sentence[i], end="")
                i += 1
            print(sentence[i], end="")
            i += 1
        elif (sentence[i] == ' '):
            if(len(temp_word)>0):
                for w in range(len(temp_word) - 1, -1, -1):
                    print(temp_word[w], end="")
                print(sentence[i], end="")
                temp_word.clear()
                i += 1

            else:
                print(" ")
                i += 1

        elif (sentence[i] == "\n"):
            if (len(temp_word) > 0):
                for w in range(len(temp_word)- 1, -1, -1):
                    print(temp_word[w], end = "")
                print(sentence[i], end= "")
                temp_word.clear()
                i += 1

            else:
                print("\n")
                i += 1

        else:
            temp_word.append(sentence[i])
            i += 1

if __name__ == '__main__':
    sentence = sys.stdin.readline()
    reverse(sentence)
