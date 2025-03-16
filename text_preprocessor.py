import re
from unicodedata import normalize

def is_full_width_digit(char):
    return char >= u'\uff10' and char <= u'\uff19'
    
def is_full_width_alphabet(char):
    return (char >= u'\uff21' and char <= u'\uff3a') or (char >= u'\uff41' and char <= u'\uff5a')

def preprocess_text(text: str):
    """
    Remove wrapping "「」"
    """
    ret = text
    ret = re.sub(r'\[.*?\]', "", ret)
    ret = re.sub(r'%.*?;', "", ret)
    ret = re.sub(r'%r', "", ret)
    ret = re.sub(r'#.*?;', "", ret)
    ret = re.sub(r'^[「『]', '', ret)
    ret = re.sub(r'[」』]$', '', ret)
    ret = re.sub(r'[\u3000\n(\\n)]', '', ret)
    ret = ret.replace('『', '“').replace('』', '”')

    ret = ''.join([chr(ord(c) - 0xfee0) if is_full_width_digit(c) or is_full_width_alphabet(c) else c for c in ret])

    return ret
