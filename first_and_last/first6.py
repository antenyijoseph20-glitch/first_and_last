def censor_words(text, banned_word):
    if not banned_word or not text:
        return text
    
    b_len = 0
    for _ in banned_word:
        b_len += 1
        
    t_len = 0
    for _ in text:
        t_len += 1
        
    result = ""
    i = 0
    while i < t_len:
        match = True
        if i + b_len > t_len:
            match = False
        else:
            for j in range(b_len):
                if text[i + j] != banned_word[j]:
                    match = False
                    break
        
        if match:
            result += "***"
            i += b_len
        else:
            result += text[i]
            i += 1
            
    return result