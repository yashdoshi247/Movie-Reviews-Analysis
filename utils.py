import numpy as np
import re
import pickle
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

file_path = 'preprocessor.pickle'
with open(file_path,'rb') as f:
    preprocessor_pipeline = pickle.load(f)

def text_preprocessor(text):
    # Remove HTML tags
    preprocessed_text = re.sub('<[^>]*>', '', text)

    # Remove punctuation
    preprocessed_text = re.sub(r'[^\w\s]', '', preprocessed_text)

    # Convert to lowercase
    preprocessed_text = preprocessed_text.lower()

    #Lemmatize and remove stopwords
    lemmatizer=WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    preprocessed_text=' '.join(lemmatizer.lemmatize(word) for word in preprocessed_text.split()
                                                        if word not in stop_words)
    
    preprocessed_text = preprocessor_pipeline.transform([preprocessed_text])

    return preprocessed_text
    
    
    
