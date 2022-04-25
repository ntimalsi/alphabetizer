from collections import Counter
alphas=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t'
        ,'u','v','w','x','y','z'
        ]

word="3 Blind Mice"
counts=Counter(word)

for i in alphas:
    if i in word:
        print(counts[i]*i,end="")
    if i.upper() in word:
        print(counts[i.upper()]*i.upper(),end="")