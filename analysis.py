import numpy as np
import string
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer


def generate_scores(name):

    with open("speech-to-text3/transcript_files/" + name + ".txt") as f:
        reference = f.readlines()
    with open("speech-to-text3/output_files/" + name + "_output.txt") as f:
        hypothesis = f.readlines()

    reference_str = ""
    for lines in reference:
        reference_str += lines

    hypothesis_str = ""
    for lines in hypothesis:
        hypothesis_str += lines

    hypothesis = hypothesis_str.lower()
    reference = reference_str.lower()

    accuracy = get_accuracy(reference, hypothesis)
    wer = get_wer(reference, hypothesis)
    cos_sim = cosine_sim(reference, hypothesis)

    return (accuracy, wer, cos_sim)


def get_wer(reference, hypothesis):
    ref_words = reference.split()
    hyp_words = hypothesis.split()
    d = np.zeros((len(ref_words) + 1, len(hyp_words) + 1))
    for i in range(len(ref_words) + 1):
        d[i, 0] = i
    for j in range(len(hyp_words) + 1):
        d[0, j] = j
    for i in range(1, len(ref_words) + 1):
        for j in range(1, len(hyp_words) + 1):
            if ref_words[i - 1] == hyp_words[j - 1]:
                d[i, j] = d[i - 1, j - 1]
            else:
                substitution = d[i - 1, j - 1] + 1
                insertion = d[i, j - 1] + 1
                deletion = d[i - 1, j] + 1
                d[i, j] = min(substitution, insertion, deletion)

    wer = d[len(ref_words), len(hyp_words)] / len(ref_words)
    return wer


def normalize(text):
    text = text.split()
    return text


def cosine_sim(text1, text2):
    vectorizer = TfidfVectorizer(tokenizer=normalize)
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0, 1]


def get_accuracy(reference, hypothesis):
    ref_words = reference.split()
    hyp_words = hypothesis.split()
    d = np.zeros((len(ref_words) + 1, len(hyp_words) + 1))
    for i in range(len(ref_words) + 1):
        d[i, 0] = i
    for j in range(len(hyp_words) + 1):
        d[0, j] = j
    for i in range(1, len(ref_words) + 1):
        for j in range(1, len(hyp_words) + 1):
            if ref_words[i - 1] == hyp_words[j - 1]:
                d[i, j] = d[i - 1, j - 1]
            else:
                d[i, j] = d[i - 1, j - 1] + 1

    accuracy = d[len(ref_words), len(hyp_words)] / len(ref_words)
    return accuracy
