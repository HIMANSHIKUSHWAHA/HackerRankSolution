#Link to problem: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n=int(input())
    arr=list(map(int, input().split()))
    a=list(set(arr))
    a.sort(reverse=True)
    b=a[1]
    print(b)