import re
"""
Name: Trever Cluney
Date: 01/24/22
Email: tlcluney@dmacc.edu
Overview: Using regex to parse information
"""


if __name__ == '__main__':
    search_string = "“I must not fear. Fear is the mind-killer." \
                    " Fear is the little-death that brings total obliteration." \
                    " I will face my fear. I will permit it to pass over me and through me." \
                    " And when it has gone past I will turn the inner eye to see its path." \
                    " Where the fear has gone there will be nothing. Only I will remain.” – Frank Herbert, Dune"
    all_f_results = len(re.findall('f', search_string, flags=re.IGNORECASE))
    beginning_f_results = len(re.findall(r'\bf', search_string, flags=re.IGNORECASE))
    all_not_results = len(re.findall('\snot\s', search_string, flags=re.IGNORECASE))
    print(f"How many words contain the letter f (case insensitive)? {all_f_results}")
    print(f"How many words start the letter f (case insensitive)? {beginning_f_results}")
    print(f"How many times the word \"not\" appears (whole word only)? {all_not_results}")
    updated_search_string = re.sub(r"I\s", "You ", search_string)
    updated_search_string = re.sub(r"\smy\s", " your ", updated_search_string)
    updated_search_string = re.sub(r"\sme\s", " you ", updated_search_string)
    updated_search_string = re.sub(r"\sme.", " you.", updated_search_string)
    print(updated_search_string)

    pass
