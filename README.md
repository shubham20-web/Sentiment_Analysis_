*Sentiment Analysis using Machine Learning

A Machine Learning based Sentiment Analysis system built using Python, NLP, and Scikit-learn to classify text into positive, negative, or neutral sentiment.

The project demonstrates a complete Natural Language Processing pipeline including text preprocessing, feature extraction, model training, and evaluation.

Tech Stack

Python

NLTK

Scikit-learn

Pandas

NumPy

Matplotlib

Seaborn

Features

Text preprocessing using NLP techniques

Stopword removal and text cleaning

Lemmatization using NLTK

TF-IDF feature extraction

Machine Learning model training

Sentiment classification

Model evaluation using accuracy score

End-to-end NLP pipeline

Architecture

Text Data
↓
Text Preprocessing
↓
Tokenization & Stopword Removal
↓
TF-IDF Vectorization
↓
Train/Test Split
↓
SVM Model Training
↓
Sentiment Prediction

Project Workflow
1 Data Loading

The dataset containing text and sentiment labels is loaded using Pandas.

import pandas as pd
data = pd.read_excel("dataset.xlsx")
2 Text Preprocessing

Steps performed:

Lowercasing

Removing punctuation

Tokenization

Stopword removal

Lemmatization

Libraries used:

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
3 Feature Engineering

Text data is converted into numerical vectors using TF-IDF Vectorizer.

from sklearn.feature_extraction.text import TfidfVectorizer

TF-IDF helps represent the importance of words in a document.

4 Train Test Split

The dataset is split into training and testing data.

from sklearn.model_selection import train_test_split
5 Model Training

A Support Vector Machine (SVM) classifier is used for sentiment classification.

from sklearn.svm import SVC

SVM performs well for text classification tasks.

6 Model Evaluation

The model performance is evaluated using accuracy score.

from sklearn.metrics import accuracy_score
Project Structure
Sentiment-Analysis/
│
├── Sentiment_Analysis_New.ipynb
├── dataset.xlsx
├── README.md
Installation

Clone the repository

git clone https://github.com/yourusername/sentiment-analysis.git

Move to project directory

cd sentiment-analysis

Install dependencies

pip install pandas numpy nltk scikit-learn matplotlib seaborn

Run Jupyter Notebook

jupyter notebook

Open:

Sentiment_Analysis_New.ipynb
Future Improvements

Implement Deep Learning models (LSTM / GRU)

Use BERT or Transformer models

Deploy model using Flask or FastAPI

Build a web application for sentiment prediction

Improve dataset size for better accuracy

Author

Shubham Dhadse

Aspiring Data Scientist
Interested in Machine Learning | NLP | Generative AI

⭐ If you like this project, feel free to star the repository.
