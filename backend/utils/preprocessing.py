import re, string
import numpy as np
from collections import Counter
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag

stop_words = set(stopwords.words("english"))
contractions = {"'s","'ve","'re","n't","'ll","'d","'m"}

def preprocess_text(text):
    text =  text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text).strip()
    return text


def extract_advanced_features(text):
    features = {}

    # Tokenization
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    total_words = len(words)
    total_sentences = len(sentences) if sentences else 1
    
    # --- Lexical Features ---
    features["avg_word_len"] = np.mean([len(w) for w in words]) if words else 0
    features["vocab_richness"] = len(set(words)) / total_words if total_words > 0 else 0
    word_counts = Counter(words)
    hapax_legomena = [w for w, c in word_counts.items() if c == 1]
    features["hapax_ratio"] = len(hapax_legomena) / total_words if total_words > 0 else 0
    
    # --- Syntactic Features ---
    pos_tags = pos_tag(words)
    pos_counts = Counter(tag for _, tag in pos_tags)
    total_pos = sum(pos_counts.values()) if pos_counts else 1
    features["noun_ratio"] = pos_counts.get("NN", 0) / total_pos
    features["verb_ratio"] = pos_counts.get("VB", 0) / total_pos
    features["adj_ratio"] = pos_counts.get("JJ", 0) / total_pos
    features["adv_ratio"] = pos_counts.get("RB", 0) / total_pos
    
    # Sentence structure
    sentence_lengths = [len(word_tokenize(s)) for s in sentences]
    features["avg_sentence_len"] = np.mean(sentence_lengths) if sentence_lengths else 0
    features["sentence_len_var"] = np.var(sentence_lengths) if len(sentence_lengths) > 1 else 0  # burstiness
    
    # --- Stylistic Features ---
    features["punctuation_ratio"] = sum(1 for w in words if re.match(r"[^\w\s]", w)) / total_words if total_words > 0 else 0
    features["stopword_ratio"] = sum(1 for w in words if w.lower() in stop_words) / total_words if total_words > 0 else 0
    features["contraction_ratio"] = sum(1 for w in words if w.lower() in contractions) / total_words if total_words > 0 else 0
    
    # --- Repetition Features ---
    repeated_phrases = sum(1 for w, c in word_counts.items() if c > 3)
    features["repetition_ratio"] = repeated_phrases / len(word_counts) if word_counts else 0
    
    return features
