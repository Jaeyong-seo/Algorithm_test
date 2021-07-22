#미쳤따!
def solution(n,*maps):
    return [line(n, a|b) for a,b in zip(*maps)]

def line(n,x):
    return ''.join(' #'[int(i)] for i in f'{x:016b}'[-n:])

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))