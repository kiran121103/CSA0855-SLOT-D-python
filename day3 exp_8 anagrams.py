from collections import defaultdict
def anagrams(words):
    a = defaultdict(list)
    
    for word in words:
        a["".join(sorted(word))].append(word)
        
    for b in a.values():
        print(" ".join(b))
        
if __name__ == "__main__":
    arr =  input("enter the str:")
    anagrams(arr)
