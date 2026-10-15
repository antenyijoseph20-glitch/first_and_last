from firstdrill import first_and_last
from first2 import clean_username
from first3 import get_initials
from first4 import str_len
from first5 import reverse_string
from first6 import censor_words

def run_all():
    sample_text = "Anteny jnr"
    
    print("=" * 40)
    print(" RUNNING ALL 6 PYTHON EXERCISES")
    print("=" * 40)
    
    # 1. First and Last
    print("\n[Ex 1] First and Last:")
    print(f"Input: '{sample_text}' -> Output: {first_and_last(sample_text)}")
    
    # 2. Clean Username
    username_input = "  Anteny jnr  "
    print("\n[Ex 2] Clean Username:")
    print(f"Input: '{username_input}' -> Output: '{clean_username(username_input)}'")
    
    # 3. Get Initials
    print("\n[Ex 3] Get Initials:")
    print(f"Input: '{sample_text}' -> Output: '{get_initials(sample_text)}'")
    
    # 4. Manual String Length
    print("\n[Ex 4] String Length:")
    print(f"Input: '{sample_text}' -> Output: {str_len(sample_text)}")
    
    # 5. Reverse String
    print("\n[Ex 5] Reverse String:")
    print(f"Input: '{sample_text}' -> Output: '{reverse_string(sample_text)}'")
    
    # 6. Manual Censor Words
    banned = "jnr"
    censor_input = "Welcome Anteny jnr to Python!"
    print("\n[Ex 6] Censor Words:")
    print(f"Input: '{censor_input}' (Banned: '{banned}')")
    print(f"Output: '{censor_words(censor_input, banned)}'")
    
    print("\n" + "=" * 40)

if __name__ == "__main__":
    run_all()