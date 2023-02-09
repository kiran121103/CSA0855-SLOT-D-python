def remove_common_words(s1, s2):
    words1 = set(s1.split())
    words2 = set(s2.split())
    common_words = words1 & words2
    s1 = " ".join(word for word in s1.split() if word not in common_words)
    s2 = " ".join(word for word in s2.split() if word not in common_words)
    return s1, s2

s1 = input("Enter the first sentence:")
s2 = input("Enter the second sentence:")
s1, s2 = remove_common_words(s1, s2)
print("After removing common words")
print("Sentence 1:", s1)
print("Sentence 2:", s2)
