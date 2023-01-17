# Data Preparation
**Extract content from XML file**
```
python -m wikiextractor.WikiExtractor ~/Desktop/Wikipedia/NE/newiki-latest-pages-articles.xml 
```

**Combine all text into a single file**
```
cat text/*/* > newiki-latest-pages-article.txt 
```

**Remove HTML tags and extra space**
```
cat newiki-latest-pages-article.txt | sed '/^<doc/d' | sed '/^<\/doc/d' | sed '/&lt;.*&gt;/d' | sed '/^$/d' > wiki.txt
```

**Train**
This will read from `wiki.txt` file.
```
python train.py
```

**Test**
Run the following in either console or from file.
```py
from gensim.models import Word2Vec

model = Word2Vec.load("word2vec.model")

model.wv.most_similar(positive=["गाई"])
```