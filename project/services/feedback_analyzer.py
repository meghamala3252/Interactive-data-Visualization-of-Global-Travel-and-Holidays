from collections import Counter

def analyze_feedback(feedback_text):
    """
    Simple keyword-based classifier. 
    In production, use HuggingFace Transformers (Zero-shot classification).
    """
    text = feedback_text.lower()
    
    if any(word in text for word in ['bug', 'error', 'broken', 'fail', 'crash']):
        category = 'Bug'
        sentiment = 'Negative'
    elif any(word in text for word in ['feature', 'add', 'would like', 'suggest']):
        category = 'Feature Request'
        sentiment = 'Neutral'
    elif any(word in text for word in ['good', 'great', 'awesome', 'love', 'helpful']):
        category = 'General'
        sentiment = 'Positive'
    else:
        category = 'Confusion'
        sentiment = 'Neutral'
        
    return category, sentiment
