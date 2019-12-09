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




location_tagger("Description: I-64 at MM 279.3 - City of Norfolk, near Chesapeake Boulevard, major delays - a vehicle accident. The WB left shoulder and left lane are closed. backups ~ 5.0 miles. Last updated: Thu 11/07/2019 6:14 PM EST".lower())