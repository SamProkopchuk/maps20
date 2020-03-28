N = int(input())
D = {}

def get_filtered_wrd(word):
    word = word.lower()
    word = word.replace('-',' ')
    return word


for i in range(N):
    word = input()
    filtered = get_filtered_wrd(word)
    if not filtered in D:
        D[filtered] = 0 # 0
    else:
        D[filtered]+=1

print(N-sum(D[key] for key in D.keys()))
