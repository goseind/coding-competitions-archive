def k_goodness(S, K):
    X = 0
    i = 0

    while i < (len(S)-1)/2:
        if S[i] != S[len(S)-1-i-1]:
            X += 1
        i += 1

    if X == K:
        return 0
    elif X > K:
        return X - K
    elif X < K:
        return K - X

file = open('data/secret/subtask1/1.in', 'r')
lines = file.readlines()

result = open('data/secret/subtask1/1.ans', 'r')
results = result.readlines()

T = int(lines[0])
i = 2
c = 1
j = 1

while j <= T:
    i1, i2 = map(int, lines[i-1].split())
    ops = k_goodness(lines[i], i2)

    print("Case #{}: {}".format(c, ops))

    s1 = "Case #{}: {}".format(c, ops)
    s2 = results[j-1]
    
    if s1 == s2:
        print("Correct!")

    c += 1
    i += 2
    j += 1
