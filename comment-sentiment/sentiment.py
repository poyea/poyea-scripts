"""                                                                
     ██╗ ██████╗ ██╗  ██╗███╗   ██╗    ██╗      █████╗ ██╗    ██╗
     ██║██╔═══██╗██║  ██║████╗  ██║    ██║     ██╔══██╗██║    ██║
     ██║██║   ██║███████║██╔██╗ ██║    ██║     ███████║██║ █╗ ██║
██   ██║██║   ██║██╔══██║██║╚██╗██║    ██║     ██╔══██║██║███╗██║
╚█████╔╝╚██████╔╝██║  ██║██║ ╚████║    ███████╗██║  ██║╚███╔███╔╝
 ╚════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝    ╚══════╝╚═╝  ╚═╝ ╚══╝╚══╝ 
=============== Sentiment 2020 ===============
"""
import re
from typing import Dict, List

import nltk

nltk.download("stopwords")

POS_LIST = "positive-words.txt"
NEG_LIST = "negative-words.txt"

COM_LIST = "comments.txt"


def analyse(list_of_comments: List[str], dictionary: Dict[str, int]) -> int:
    """
    Time-optimized function to compute the overal sentiment score.

    We first conut the occurrence of each word. Then, we look up our lists of words.

    Returns a sentiment score between -1 and 1, representing the polarity.
    """
    d = {}
    score = 0
    cnt = 0
    for comment in list_of_comments:
        if comment in d:
            d[comment] += 1
        else:
            d[comment] = 1
        if len(comment) > 0 and comment != " ":
            cnt += 1
    for word, polarity in dictionary.items():
        if word in d:
            score += polarity * d[word]
    return score / cnt


def preprocess(list_of_comments: List[str]) -> List[str]:
    """
    Preprocess function to remove:
        1.) tabs at the end
        2.) URL
        3.) special unicode characters
        4.) ASCII characters
        5.) Stop words: prepositions, articles, pronouns, conjunctions
    and to replace dashes "-" and slashes "/" with spaces.

    Returns the processed list.
    """
    # 1.)
    to_erase = re.compile(r"\b(\t\d)$")
    list_of_comments = [to_erase.sub("", line) for line in list_of_comments]
    # 2.)
    to_erase_website_re = re.compile(r"https?://\S+")
    list_of_comments = [to_erase_website_re.sub("", line) for line in list_of_comments]
    # 4.)
    to_erase_re = re.compile("[.;:!'?,\"()\[\]\+]")
    list_of_comments = [
        to_erase_re.sub("", line.lower().strip()) for line in list_of_comments
    ]
    # 3.)
    unicode_re = re.compile("[\u201C\u2018\u2019\u201D]+", re.UNICODE)
    list_of_comments = [unicode_re.sub("", line) for line in list_of_comments]
    # dashes, slashes
    dash_re = re.compile("[-/]")
    list_of_comments = [dash_re.sub(" ", line) for line in list_of_comments]
    # split each comment
    list_of_comments = [line.split(" ") for line in list_of_comments]
    # flatten to 1D array
    flat_list_of_comments = []
    for sublist in list_of_comments:
        for item in sublist:
            flat_list_of_comments.append(item)
    # 5.)
    stop_words = set(nltk.corpus.stopwords.words("english"))
    list_of_comments = [w for w in flat_list_of_comments if not w in stop_words]
    return list_of_comments


if __name__ == "__main__":
    positive = []
    negative = []
    comments = []
    with open(POS_LIST, "r", encoding="ISO-8859-1") as txt:
        positive = txt.read().split("\n")
        positive = [x for x in positive if len(x) > 0 and next(iter(x), None) != ";"]
    with open(NEG_LIST, "r", encoding="ISO-8859-1") as txt:
        negative = txt.read().split("\n")
        negative = [x for x in negative if len(x) > 0 and next(iter(x), None) != ";"]
    with open(COM_LIST, "r", encoding="utf-8") as txt:
        comments = txt.read().split("\n")
    dictionary = {}
    for pword in positive:
        dictionary[pword] = 1
    for nword in negative:
        dictionary[nword] = -1
    print(f"Number of comments received: {len(comments)}")
    comments = preprocess(comments)
    print(f"The overall sentiment score: {analyse(comments, dictionary)}")
