ptdf = open("project_twitter_data.csv", "r")
rdf = open("resulting_data.csv", "w")

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
pc = punctuation_chars
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


# my previous functions
def strip_punctuation(s):
    for each_item in pc:
        s = s.replace(each_item, '')
    return s


def get_pos(st):
    st = strip_punctuation(st)
    ls = st.split()

    count = 0
    for each_word in ls:
        for positiveWord in positive_words:
            if each_word == positiveWord:
                count += 1
    return count

def get_neg(st):
    st = strip_punctuation(st)
    ls = st.split()

    count = 0
    for each_word in ls:
        for negativeWord in negative_words:
            if each_word == negativeWord:
                count += 1
    return count


def writeInDataFile(rdf):
    rdf.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    rdf.write("\n")

    lptdf = ptdf.readlines()
    headerDontUsed = lptdf.pop(0)
    for lines in lptdf:
        tdl = lines.strip().split(',')
        rdf.write("{}, {}, {}, {}, {}".format(tdl[1], tdl[2], get_pos(tdl[0]), get_neg(tdl[0]),
                                              (get_pos(tdl[0]) - get_neg(tdl[0]))))
        rdf.write("\n")


writeInDataFile(rdf)
ptdf.close()
rdf.close()