t = int(input())

for _ in range(t):
    sounds = list(map(str, input().split()))

    while True:
        n = input()
        if n == "what does the fox say?":
            break
        
        voice = list(map(str, n.split()))

        for i in range(len(sounds)):
            if sounds[i] == voice[2]:
                sounds[i] = sounds[i].replace(voice[2], "")
    
    for s in sounds:
        if s:
            print(s, end=' ')