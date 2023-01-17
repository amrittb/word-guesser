from gensim.models import Word2Vec
from indicnlp.tokenize import sentence_tokenize, indic_tokenize
from tqdm import tqdm

def main():
	tokenized_text = []
	with open("wiki.txt", "r") as file:
		for line in tqdm(file):
			sentences = sentence_tokenize.sentence_split(line, lang="np")

			for sentence in sentences:
				tokenized_text.append(indic_tokenize.trivial_tokenize(sentence))
			
	model = Word2Vec(sentences=tokenized_text, vector_size=100, window=5, min_count=1, workers=4)
	model.save("word2vec.model")

if __name__ == "__main__":
	main()