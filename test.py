from gensim.models import Word2Vec

def main():
    model = Word2Vec.load("word2vec.model")

    for item in model.wv.most_similar(positive=["गाई"]):
        print(item[0])

if __name__ == "__main__":
    main()
