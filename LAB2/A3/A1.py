import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter

nltk.download('punkt_tab')

# Sample paragraph
text = """Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence.
It focuses on the interaction between computers and humans through natural language.
The ultimate goal of NLP is to enable computers to understand, interpret, and generate human language.
It involves tasks such as speech recognition, machine translation, and text summarization."""

# Preprocessing: Remove special characters and digits
clean_text = re.sub(r'[^A-Za-z\s]', '', text)

# Tokenization
sentences = sent_tokenize(text)
words = word_tokenize(clean_text.lower())

# Word frequency
word_freq = Counter(words)

# Sentence scoring
sentence_scores = {}
for sent in sentences:
    for word in word_tokenize(sent.lower()):
        if word in word_freq:
            if sent not in sentence_scores:
                sentence_scores[sent] = word_freq[word]
            else:
                sentence_scores[sent] += word_freq[word]

# Extract top sentences
summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:2]
summary = " ".join(summary_sentences)

# Output summary
print("Summary:")
print(summary)

