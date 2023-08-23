# Demo of Advanced Topic: Function Files and Dictionaries

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
pc = punctuation_chars
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


def strip_punctuation(s):
    for each_item in pc:
        s = s.replace(each_item, '')
    return s


def get_pos(st):
    st = strip_punctuation(st)
    ls = st.split()
    ls = st.lower()

    count = 0
    for each_word in ls:
        for positiveWord in positive_words:
            if each_word == positiveWord:
                count += 1
    return count


txt = "Hello my FRIENDS"
x = txt.lower()
print(x)