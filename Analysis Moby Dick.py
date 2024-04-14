import requests
from bs4 import BeautifulSoup
import nltk
from collections import Counter
nltk.download('stopwords')


url = 'https://s3.amazonaws.com/assets.datacamp.com/production/project_147/datasets/2701-h.htm'

r = requests.get(url)

r.encoding = 'utf-8'

text = r.text

soup = BeautifulSoup(text, 'html.parser')

moby_text = soup.get_text()


tokenizer = nltk.tokenize.RegexpTokenizer('\w+')

tokens = tokenizer.tokenize(moby_text)

words_no_stop = [word.lower() for word in tokens if word.lower() not in nltk.corpus.stopwords.words('english')]


c = Counter(words_no_stop)

top10 = c.most_common(10)

print(top10)
