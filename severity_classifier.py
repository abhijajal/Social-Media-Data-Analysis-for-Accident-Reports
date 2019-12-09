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


def severity_finder(txt):

	# Sample text:
	#txt = "No injuries reported in three-car accident this morning."
	nlp = spacy.load("en_core_web_sm")
	txt = txt.lower()
	doc = nlp(txt)
	lems = [x.lemma_ for x in doc]
	lems = " ".join(lems)
	doc2 = nlp(lems)

	# instantiate a new Matcher class object
	matcher = Matcher(nlp.vocab)

	# define the pattern for matcher
	pattern1 = [{'POS': {'IN': ['NUM', 'ADJ', 'NOUN']}},
					{'LOWER': {'IN': ['accident', 'accidents', 'incident', 'injury', 'damage', 'death']}, 'POS': 'NOUN'}]
	pattern2 = [{'LOWER': {'IN': ['no', 'none', 'major', 'minor', 'severe']}},
					{'LOWER': {'IN': ['injured', 'injury', 'injure', 'hurt', 'damage', 'accident']}}]
	pattern3 = [{'POS': {'IN': ['NUM', 'ADJ', 'NOUN']}},
					{'LOWER': {'IN': ['injured', 'injury', 'injure', 'kill', 'die', 'damage', 'hit', 'bruise', 'crash']}, 'POS': 'VERB'}]
	pattern4 = [{'POS': 'NUM'}, {'LOWER': {
			'IN': ['vehicle', 'car', 'truck', 'semi', 'van', 'sedan', 'people', 'pedestrian', 'suv', 'person', 'bike',
				   'motorcycle', 'automobile', 'auto', 'bus', 'cyclist', 'buggy', 'cruiser']}}]

	# add the pattern to the previously created matcher object
	matcher.add("Matching", None, pattern1, pattern2, pattern3, pattern4)

	#print("\n", lems, "\n")

	matches = matcher(doc2)
	spans = list()

	for match_id, start, end in matches:
		#print("****matching phrases***")
		# string_id = nlp.vocab.strings[match_id]
		span = doc[start:end]
		# print(span.text)
		spans.append(span)

	if len(spans)==0:
		spans.append("unknown severity")

	#print(spans)

	return spans

