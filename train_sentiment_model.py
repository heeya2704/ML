import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

def train_and_save_sentiment_model():
    print("Training Flipkart Review Sentiment Model with expanded dataset...")
    
    # Expanded Flipkart product reviews dataset
    reviews = [
        # Positive Reviews (Label 1)
        "Great product, excellent quality and fast delivery!",
        "Very good performance, highly recommended purchase!",
        "Value for money, works nicely and looks awesome.",
        "Superb battery life, crisp display and awesome camera!",
        "Nice design, comfortable to use and good value.",
        "The camera quality is excellent, sharp display and great value for money!",
        "Product arrived in perfect condition, super fast shipping and high quality!",
        "Fantastic purchase! Loved the sound quality and build.",
        "Totally satisfied with this phone, smooth performance.",
        "Awesome packaging, fast delivery and top quality item.",

        # Negative Reviews (Label 0)
        "Worst item ever, poor build quality and damaged piece.",
        "Horrible experience, stopped working within two days.",
        "Cheap quality material, totally useless and bad experience.",
        "Extremely disappointed with this purchase, complete waste of money.",
        "Tasted bad, stale packaging and terrible customer support.",
        "Very bad product, battery drains rapidly and customer service is unhelpful.",
        "Defective piece received, stopped charging within a week. Very poor.",
        "Waste of money, poor response time and broken buttons.",
        "Terrible sound quality, uncomfortable fit and cheap plastics.",
        "Fake product delivered, completely useless and bad seller response."
    ]
    
    labels = [1]*10 + [0]*10
    
    # Create scikit-learn Pipeline with TF-IDF Vectorizer and Logistic Regression Classifier
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(ngram_range=(1, 2), min_df=1)),
        ('clf', LogisticRegression())
    ])
    
    # Fit model on training dataset
    pipeline.fit(reviews, labels)
    print("Model training completed.")
    
    # Save trained pipeline model to pickle file
    model_filename = 'review_sentiment_model.pkl'
    with open(model_filename, 'wb') as f:
        pickle.dump(pipeline, f)
        
    print(f"Model saved to '{model_filename}'.")

if __name__ == '__main__':
    train_and_save_sentiment_model()
