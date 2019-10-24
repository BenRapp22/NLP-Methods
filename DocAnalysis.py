# This program takes value counts from a text-based dataset in which there are groups of documents contained in
# a corpus made up of 5 collections. Additionally, the program locates a given string and counts its frequency across
# all documents in a given collection, returning a dataframe containing only the rows containing the given phrase.

# GLOSSARY:
# "term" = the string whose frequency is being counted by term_finder
# "collection" = A labeled subset of documents in the corpus
# "subgroup" = A labeled subset of each collection
# "text" = The body of text contained in a document
# "text_id = The numerical identifier associated with each document
# "text_name" = The "title" of a given document

import pandas as pd
import numpy as np

path = 'path'
sub_folder = 'AnalysisStats'
file_name = 'Analysis'

df = pd.read_csv(path + file_name + '.csv', sep=",", header=0, engine='python')


# Locating term
def term_finder(data):
    t = "term"
    term_array = data['text'].values
    term_count = []
    for i in range(0, len(term_array)):
        if t in term_array[i]:
            term_count.append(i)
    term_count = np.array(term_count)

    raw_id_array = data['text_id'].values
    id_list = []
    for j in range(0, len(term_count)):
        id_list.append(raw_id_array[term_count[j]])
    id_list = np.array(id_list)

    term_text = []
    for k in range(0, len(term_count)):
        term_text.append(term_array[term_count[k]])
    term_text = np.array(term_text)

    term_frame = data.loc[data['text_id'].isin(id_list)]
    print("--------------------")
    return term_frame


# List of Collections
collection_list = df['collection_name'].drop_duplicates()
print('COLLECTION LIST:')
print(collection_list)
collection_list.to_csv(path + sub_folder + '/outlets_list.csv', sep=",", encoding='utf-8')
print("--------------------")

# Number of Documents per Collection
print('NUMBER OF DOCUMENTS PER COLLECTION:')
s = df.groupby(['collection_name', 'text_id']).agg({'text_id': sum})
a_per_s = s.groupby(['collection_name']).size().reset_index(entity_name='count')
# a_per_s.to_csv(path + sub_folder + '/Articles_per_Source.csv', sep=',', encoding='utf-8')
a_per_s = a_per_s.sort_values(by=['count'], ascending=False)
top_sources = a_per_s.head(5)
print('---------------------')

# Documents from Collection 1
print("DOCUMENTS FROM COLLECTION 1 CONTAINING TERM")
c1 = df[df['collection_name'] == "Collection 1"]
c1 = c1[['text_id', 'text_name', 'text']]
c1.to_csv(path + sub_folder + '/collection1_articles.csv', sep=",", encoding='utf-8')
print(term_finder(c1))
print("---------------------")

# Documents from Collection 2
print("DOCUMENTS FROM COLLECTION 2 CONTAINING TERM")
c2s1 = df[df['collection_name'] == "Collection 2 Subgroup 1"]
c2s2 = df[df['collection_name'] == "Collection 2 Subgroup 2 "]
c2s3 = df[df['collection_name'] == "Collection 2 Subgroup 3"]
c2 = pd.concat([c2s1, c2s2, c2s3])
c2 = c2[['text_id', 'text_name', 'text']]
c2.to_csv(path + sub_folder + '/collection2_articles.csv', sep=",", encoding='utf-8')
print(term_finder(c2))
print("----------------------")

# Documents from Collection 3
print("DOCUMENTS FROM Collection 3 CONTAINING TERM")
c3s1 = df[df['collection_name'] == "Collection 3 Subgroup 1"]
c3s2 = df[df['collection_name'] == "Collection 3 Subgroup 2"]
c3 = pd.concat([c3s1, c3s2])
c3 = c3[['text_id', 'text_name', 'text']]
c3.to_csv(path + sub_folder + '/collection3_articles.csv', sep=",", encoding='utf-8')
print(term_finder(c3))
print("----------------------")

# Documents from Collection 4
print("DOCUMENTS FROM COLLECTION 4 CONTAINING TERM")
c4 = df[df['collection_name'] == "Collection 4"]
c4 = c4[['text_id', 'text_name', 'text']]
c4.to_csv(path + sub_folder + '/collection4_articles.csv', sep=",", encoding='utf-8')
print(term_finder(c4))
print("----------------------")

# Documents from Collection 5
print("DOCUMENTS FROM COLLECTION 5 CONTAINING TERM")
c5 = df[df['collection_name'] == "Collection 5"]
c5 = c5[['text_id', 'text_name', 'text']]
c5.to_csv(path + sub_folder + '/collection5_articles.csv', sep=",", encoding='utf-8')
print(term_finder(c5))
print("----------------------")

# Total Number of Documents
print("TOTAL NUMBER OF DOCUMENTS:")
num_doc = df['text_id'].drop_duplicates().count()
print(num_doc)
print("----------------------")

