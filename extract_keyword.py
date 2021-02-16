from rake_nltk import Rake
import rake_nltk

rake_nltk_var = Rake()

text = """ I am a programmer from Brazil, and I am here to guide you 
with Data Science, Machine Learning, Python, Java and C++ for free. 
I hope you will learn a lot in your journey towards Coding, 
Machine Learning and Artificial Intelligence with me."""

rake_nltk_var.extract_keywords_from_text(text)
keyword_extracted = rake_nltk_var.get_ranked_phrases()
print(keyword_extracted)