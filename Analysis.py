import pandas as pd
import numpy as np


path = 'data/'
sub_folder = 'ArticleAnalysisStat'
file_name = 'clean_ArticleAnalysis1'

df = pd.read_csv(path + file_name + '.csv', sep=",", header=0, engine='python')

print(df.columns)
print(df.shape[0])

# Locating Trump


def trump_finder(data):
    t = "Trump"
    tarray = data['extracttext'].values
    tcount = list()
    for i in range(0, len(tarray)):
        if t in tarray[i]:
            tcount.append(i)
    tcount = np.array(tcount)

    raw_id_array = data['articleid'].values
    id_list = list()
    for j in range(0, len(tcount)):
        id_list.append(raw_id_array[tcount[j]])
    id_list = np.array(id_list)

    trump_text = list()
    for k in range(0, len(tcount)):
        trump_text.append(tarray[tcount[k]])
    trump_text = np.array(trump_text)

    trump_frame = data.loc[data['articleid'].isin(id_list)]
    return trump_frame
    print("--------------------")


# List of Outlets
outlet_list = df['name'].drop_duplicates()
print('OUTLET LIST:')
print(outlet_list)
outlet_list.to_csv(path + sub_folder + '/outlets_list.csv', sep=",", encoding='utf-8')
print("--------------------")

# Number of Articles per Outlet
print('NUMBER OF ARTICLES PER OUTLET:')
s = df.groupby(['name', 'articleid']).agg({'articleid': sum})
a_per_s = s.groupby(['name']).size().reset_index(name='count')
# a_per_s.to_csv(path + sub_folder + '/Articles_per_Source.csv', sep=',', encoding='utf-8')
a_per_s = a_per_s.sort_values(by=['count'], ascending=False)
top_sources = a_per_s.head(5)
print(top_sources)
print('---------------------')

# Articles from Washington Post
print("ARTICLES FROM THE WASHINGTON POST CONTAINING TRUMP")
wp = df[df['name'] == "washingtonpost"]
wp = wp[['articleid', 'title', 'extracttext']]

wp.to_csv(path + sub_folder + '/wp_articles_colab.csv', sep=",", encoding='utf-8')
print("---------------------")


# Articles from Huffington Post
print("ARTICLES FROM HUFFINGTON POST CONTAINING TRUMP")
hp1 = df[df['name'] == "Huffington Post"]
hp2 = df[df['name'] == "Huffington Post UK"]
hp3 = df[df['name'] == "Huffington Post Canada"]
hp = pd.concat([hp1, hp2, hp3])
hp = hp[['articleid', 'title', 'extracttext']]
hp.to_csv(path + sub_folder + '/hp_articles_colab.csv', sep=",", encoding='utf-8')
print(trump_finder(hp))
print("----------------------")


# Articles from ABC News
print("ARTICLES FROM ABC NEWS CONTAINING TRUMP")
abc1 = df[df['name'] == "ABC News"]
abc2 = df[df['name'] == "ABC Online"]
abc = pd.concat([abc1, abc2])
abc = abc[['articleid', 'title', 'extracttext']]
abc.to_csv(path + sub_folder + '/abc_articles_colab.csv', sep=",", encoding='utf-8')
print(trump_finder(abc))
print("----------------------")

# Articles from POLITICO Magazine
print("ARTICLES FROM POLITICO MAGAZINE CONTAINING TRUMP")
politico = df[df['name'] == "POLITICO Magazine"]
politico = politico[['articleid', 'title', 'extracttext']]
politico.to_csv(path + sub_folder + '/politico_articles_colab.csv', sep=",", encoding='utf-8')
print(trump_finder(politico))
print("----------------------")

# Articles from Daily Mail
print("ARTICLES FROM DAILY MAIL CONTAINING TRUMP")
dm = df[df['name'] == "Daily Mail"]
dm = dm[['articleid', 'title', 'extracttext']]
dm.to_csv(path + sub_folder + '/dm_articles_colab.csv', sep=",", encoding='utf-8')
print(trump_finder(dm))
print("----------------------")


# Total Number of Articles
print("TOTAL NUMBER OF ARTICLES:")
num_art = df['articleid'].drop_duplicates().count()
print(num_art)
print("----------------------")

# Hillary Mentioned

print('ARTICLES WHERE CLINTON IS MENTIONED:')
h = "Clinton"
harray = df['extracttext'].values
hcount = list()
nohcount = list()
for i in range(0, len(harray)):
    if h in harray[i]:
        hcount.append(i)
    else:
        nohcount.append(i)
hcount = np.array(hcount)
nohcount = np.array(nohcount)
print(hcount)
print('--------------------')

