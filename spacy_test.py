import re
import string
import nltk
import spacy
import pandas as pd
import numpy as np
import math
from tqdm import tqdm

from spacy.matcher import Matcher
from spacy.tokens import Span
from spacy import displacy

pd.set_option('display.max_colwidth', 200)


def num_patterns(txt):

	nlp = spacy.load("en_core_web_sm")
	doc = nlp(txt)
	print(txt)
	# Matcher class object
	matcher = Matcher(nlp.vocab)
	matcher.add("matching", None, [{'POS': 'NUM'}, {'POS': 'VERB'}], [{'POS': 'NUM'}, {'POS': 'NOUN'}])

	matches = matcher(doc)
	span=""
	for match_id, start, end in matches:
		span = doc[start:end]
		print(span.text)

	matcher2 = Matcher(nlp.vocab)
	matcher2.add("matching", None, [{'POS': 'NUM'}, {'POS': 'VERB'}], [{'POS': 'NUM'}, {'POS': 'NOUN'}])

	matches = matcher(doc)
	span = ""
	for match_id, start, end in matches:
		span = doc[start:end]
		print(span.text)


newPositiveDataSetFile = open("positiveDataset.txt", 'r+')

lines = newPositiveDataSetFile.readlines()
for eachLine in lines:

	num_patterns(eachLine)

