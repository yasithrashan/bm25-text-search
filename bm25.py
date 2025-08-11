import math

class BM25:
    def __init__(self, corpus, k1=1.5, b=0.75):
        self.corpus = [doc.split() for doc in corpus]
        self.N = len(self.corpus)
        self.avgdl = sum(len(doc) for doc in self.corpus) / self.N
        self.k1 = k1
        self.b = b
        self.df = {}
        self.idf = {}

        for doc in self.corpus:
            for word in set(doc):
                self.df[word] = self.df.get(word, 0) + 1

        for word, freq in self.df.items():
            self.idf[word] = math.log((self.N - freq + 0.5) / (freq + 0.5) + 1)

    def score(self, query, index):
        score = 0
        doc = self.corpus[index]
        doc_len = len(doc)
        freqs = {}

        for word in doc:
            freqs[word] = freqs.get(word, 0) + 1

        for word in query.split():
            if word not in self.idf:
                continue
            f = freqs.get(word, 0)
            idf = self.idf[word]
            denom = f + self.k1 * (1 - self.b + self.b * doc_len / self.avgdl)
            score += idf * (f * (self.k1 + 1)) / denom
        return score

    def search(self, query):
        scores = [(i, self.score(query, i)) for i in range(self.N)]
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores
