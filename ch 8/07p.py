def rem(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n

l=["soubhik","siddhartha","amiruddha","amit"]
print(rem(l,"s m  a"))