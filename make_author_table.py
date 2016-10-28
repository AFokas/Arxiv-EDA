#os.system('oai-harvest --set 'physics:astro-ph' http://export.arxiv.org/oai2') # download database
from __future__ import division
#!/bin/python
import numpy as np
import pandas as pd
import glob
import os
import re
import operator

#size = sum(os.path.getsize(f) for f in os.listdir('.') if os.path.isfile(f))
#print 'Size of Data : %s MB'%(size/1000000)

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

path = os.getcwd()
filenames = glob.glob(path + "/*.xml")

full_list = []

for article in filenames:
    f=open(article)
    author_list = []
    subject_list = []
    date_list = []
    for line in f:
        if 'creator' in line:
            author_list.append(find_between(line,'>','<'))
        if 'subject' in line:
            subject_list.append(find_between(line,'>','<'))
        if 'dc:date' in line:
            date = find_between(line,'>','<')
            date_year = date.split('-')[0]

            date_list.append(date_year)
    
    full_list.append([author_list[0],subject_list[0],int(date_list[0]),len(author_list)])

col = ['Author','Subject','Date','CollaborationSize']
article_info = pd.DataFrame(full_list,columns=col)


year_subject_count = {}
for year in article_info.Date.unique():
    article_year = article_info[article_info.Date == year]
    counts = article_year.Subject.value_counts()
    if int(year) > 2006:
        year_subject_count[year] = counts[0:4]

size_subject_count = {}

article_2009 = article_info[article_info.Date > 2008]
for subject in article_2009.Subject.unique():
    article_subject = article_2009[article_2009.Subject == subject]
    mean = article_subject.CollaborationSize.mean()
    size_subject_count[subject] = mean


sorted_collab = sorted(size_subject_count.items(), key=operator.itemgetter(1))

article_info_new = article_info[article_info.Date > 2008]
author_subject_count = []
mean = []
for author in article_info_new.Author.unique():
    article_author = article_info_new[article_info_new.Author == author]
    count_total = len(article_author)
    counts = len(article_author.Subject.unique())
    author_subject_count.append([author,counts,count_total])
    mean.append(counts)
import numpy as np
np.mean(mean)


### PRINT FOR ANALYSIS ###

print '##########################'
for year in year_subject_count.keys():
    print '##########################'
    print 'Top Article Entries in %s'%year
    print year_subject_count[year]
    print '##########################'
    

Collab_subject = pd.DataFrame(sorted_collab)
Collab_subject[[0,1]].to_csv('collab_subect_df.txt',index=None,sep='\t',header=False)

col = ['Author','Subjects','Articles']
author_count_df = pd.DataFrame(author_subject_count,columns = col)
author_count_df[['Subjects','Articles']].to_csv('author_count_df.txt',index=None,sep='\t',header=False)
os.system("sed -i -e 's/ /_/g' collab_subect_df.txt;sed -i -e 's/_-_/-/g' collab_subect_df.txt")

