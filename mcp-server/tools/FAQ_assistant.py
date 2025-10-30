import pandas as pd
import difflib

FAQ_PATH = "faq_arabic.csv" 
faq_df = pd.read_csv(FAQ_PATH)

def faq_assistant(question: str) -> str:
    questions = faq_df["السؤال"].tolist()
    best_match = difflib.get_close_matches(question, questions, n=1, cutoff=0.5)
    if best_match:
        answer = faq_df.loc[faq_df["السؤال"] == best_match[0], "الإجابة"].values[0]
        return f"الإجابة: {answer}"
    else:
        return "عذرًا، لم أتمكن من العثور على إجابة لهذا السؤال."