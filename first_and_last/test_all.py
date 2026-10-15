from firstdrill import first_and_last
from first2 import clean_username
from first3 import get_initials
from first4 import str_len
from first5 import reverse_string
from first6 import censor_words

def test_suite():
    print("=== RUNNING TEST SUITE (Anteny jnr) ===\n")

    # Test 1: first_and_last
    res1 = first_and_last("Anteny jnr")
    print(f"Test 1 (first_and_last): 'Anteny jnr'")
    print(f"  Got: {res1} | Expected: {{'first': 'A', 'last': 'r'}}")
    assert res1 == {"first": "A", "last": "r"}, "Test 1 Failed"

    # Test 2: clean_username
    res2 = clean_username("  Anteny jnr  ")
    print(f"\nTest 2 (clean_username): '  Anteny jnr  '")
    print(f"  Got: '{res2}' | Expected: 'anteny_jnr'")
    assert res2 == "anteny_jnr", "Test 2 Failed"

    # Test 3: get_initials
    res3 = get_initials("Anteny jnr")
    print(f"\nTest 3 (get_initials): 'Anteny jnr'")
    print(f"  Got: '{res3}' | Expected: 'A.J.'")
    assert res3 == "A.J.", "Test 3 Failed"

    # Test 4: str_len
    res4 = str_len("Anteny jnr")
    print(f"\nTest 4 (str_len): 'Anteny jnr'")
    print(f"  Got: {res4} | Expected: 10")
    assert res4 == 10, "Test 4 Failed"

    # Test 5: reverse_string
    res5 = reverse_string("Anteny jnr")
    print(f"\nTest 5 (reverse_string): 'Anteny jnr'")
    print(f"  Got: '{res5}' | Expected: 'rnj ynetnA'")
    assert res5 == "rnj ynetnA", "Test 5 Failed"

    # Test 6: censor_words
    res6 = censor_words("Anteny jnr is learning Python", "jnr")
    print(f"\nTest 6 (censor_words): 'Anteny jnr is learning Python' (banned: 'jnr')")
    print(f"  Got: '{res6}' | Expected: 'Anteny *** is learning Python'")
    assert res6 == "Anteny *** is learning Python", "Test 6 Failed"

    print("\n ALL TESTS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    test_suite()