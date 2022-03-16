def reverse_sentence(sentence):
    temp_word = list()
    result_word = list()

    for i in range(0, len(sentence)):
        if (sentence[i] != ' '):
            temp_word.append(sentence[i])

        elif (sentence[i] == ' '):
            for j in range(len(temp_word)-1, -1, -1):
                result_word.append(temp_word[j])
            result_word.append(' ')
            temp_word.clear()

        if (i == (len(sentence) - 1)):
            for j in range(len(temp_word)-1, -1, -1):
                result_word.append(temp_word[j])
            temp_word.clear()
    return result_word

if __name__ == '__main__':
    t = input()
    for i in range(int(t)):
        setence = input()
        result_word = "".join(reverse_sentence(setence))
        print(result_word)
