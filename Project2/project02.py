from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.lm import MLE
import matplotlib.pyplot as plt
import pandas as pd
import math


def create_WordCloud(documents, dimension, output_path, term_weight, stopwords):
    pass




def create_ZiphsPlot(documents, output_path): # create Zips plot
    freq_dict = dict()
    for i in documents:
        word_list = i.split()
        for word in word_list:
            if word not in freq_dict:
                freq_dict[word] = 1
            else:
                freq_dict[word] += 1
  
    freq_list = []
    for value in sorted(freq_dict.values(),reverse= True):
        freq_list.append(math.log2(value))
    
    plt.plot([math.log2(i) for i in range(1,len(freq_dict)+1)],freq_list)
    plt.xlabel('log(Rank)')
    plt.ylabel('log(Frequency)')
    plt.savefig(output_path)


def create_HeapsPlot(documents, output_path): # create Heaps plot
    pass



def create_LanguageModel(model_type, documents, max_ngram): # return the trained language model
    pass


def generate_Sentence(trained_language_model, starting_text):
    pass


def create_WordVectors(documents, dimension, model_type, window_size): # return the trained word embeddings
    pass


def use_WordRelationship(trained_WE, example_tuple, example_tuple_missing):
    pass

