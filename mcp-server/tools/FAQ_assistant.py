def faq_assistant(question: str) -> str:
    """Provide answers to frequently asked questions."""
    faq_db = {
        "What is your return policy?": "Our return policy allows returns within 30 days of purchase with a valid receipt.",
        "How can I track my order?": "You can track your order using the tracking link sent to your email after shipping.",
        "Do you offer international shipping?": "Yes, we offer international shipping to select countries. Please check our shipping policy for more details.",
        "What payment methods do you accept?": "We accept Visa, MasterCard, PayPal, and Apple Pay.",
        "How can I contact customer support?": "You can contact our customer support via email at support@example.com."
    }
    return faq_db.get(question, "Sorry, I don't have an answer for that.")