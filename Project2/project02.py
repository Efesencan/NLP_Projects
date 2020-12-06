from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.lm import MLE
from nltk.lm.models import KneserNeyInterpolated
from nltk.util import ngrams
from wordcloud import WordCloud
from nltk.corpus import stopwords
from stop_words import get_stop_words
import nltk
import matplotlib.pyplot as plt
import pandas as pd
import math

import warnings
import sys
if not sys.warnoptions:
    warnings.simplefilter("ignore")

def create_WordCloud(documents, dimension, output_path, mode, stopwords):

    all_stop_words = get_stop_words('turkish')
    additional_stopwords = ['acaba','ama','aslında','az','bazı','belki','biri','birkaç','birşey','biz','bu','çok','çünkü','da','daha','de','defa','diğer','eğer','en','gibi','hem','hepsi','her','hiç','için','ile','ise','kez','ki','kim','mi','mü','nasıl','ne','neden','nerde','nerede','nereye','niçin','niye','o','sanki','şey','şu','siz','tüm','ve','veya','ya','yani']
    all_stop_words += additional_stopwords
    
    # new_documents = []
    for i in documents:
        word_list = i.split()
    #   new_words = ""
    #     for word in word_list:
    #         if word not in stop_words:
    #             new_words+= word + " "
    #     new_documents.append(new_words)
    #     #i = [j.lower() for j in i.split() if j not in stop_words]
    #     #new_documents.append(i)
        
    if mode == "TFIDF":
        if not stopwords:
            vectorizer = TfidfVectorizer(stop_words = all_stop_words)
        else:
            vectorizer = TfidfVectorizer()
        vectorized = vectorizer.fit_transform(documents)
        feature_names = vectorizer.get_feature_names()
        dense = vectorized.todense()
        df = pd.DataFrame(dense, columns=feature_names)
        word_cloud = WordCloud(width = 800, height = 800, background_color="black").generate_from_frequencies(df.T.sum(axis=1))
        plt.imshow(word_cloud)
        plt.savefig(output_path)
        plt.clf()

    elif mode == "TF":
        if not stopwords:
            vectorizer = CountVectorizer(stop_words= all_stop_words)
        else:
            vectorizer = CountVectorizer()
        vectorized = vectorizer.fit_transform(documents)
        feature_names = vectorizer.get_feature_names()
        dense = vectorized.todense()
        df = pd.DataFrame(dense, columns=feature_names)
        word_cloud = WordCloud(width = 800,height = 800,background_color="black").generate_from_frequencies(df.T.sum(axis=1))
        
        plt.figure(figsize = (dimension,dimension))
        plt.imshow(word_cloud)
        plt.savefig(output_path)
        plt.clf()
    else:
        print("Invalid mode")

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
    term = 0
    unique_vocab = 0
    term_list = []
    unique_vocab_list = []
    freq_dict = dict()
    for i in documents:
        word_list = i.split()
        for word in word_list:
            term += 1
            term_list.append(term)
            if word not in freq_dict:
                freq_dict[word] = 1
                unique_vocab += 1
                unique_vocab_list.append(unique_vocab)
            else:
                unique_vocab_list.append(unique_vocab)

    plt.plot(term_list,unique_vocab_list)
    plt.xlabel('term occurance')
    plt.ylabel('vocabulary size')
    plt.savefig(output_path)        



def create_LanguageModel(documents, model_type, ngram): # return the trained language model
    pass


def generate_Sentence(trained_language_model, text):
    pass


def create_WordVectors(documents, dimension, model_type, window_size): # return the trained word embeddings
    pass


def use_WordRelationship(trained_WE, example_tuple, example_tuple_missing):
    pass

