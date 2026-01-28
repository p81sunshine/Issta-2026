import re
from collections import Counter
from typing import List

def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    #List words in paragraph, replacing punctuation with ' ' and all lower case
    paragraph = re.subn("[.,!?;']", ' ', paragraph.lower())[0].split(' ')
    
    #Remove any '' or words in banned from paragraph list
    paragraph = list(filter(lambda x: x in banned + [''], paragraph))
    
    #Return most common word in filtered list
    return Counter(paragraph).most_common(1)[0][0]