from posixpath import split
import arrays

def linear_recursive(arr, i, target):
    if i >= len(arr):
        return None
    elif arr[i] == target:
        return i
    else:
        return linear_recursive(arr, i+1, target)
    
def count_upper(s):
    cnt = 0
    for i in s:
        if i == "A":
            cnt += 1
            
    return cnt
            
            
def count_vowels(s, index=0):
    a = "a"
    e = "e"
    i = "i"
    o = "o"
    u = "u"
    if len(s) == index:
        return count_upper(s)
    if s[index] == a or s[index] == e or s[index] == i or s[index] == o or s[index] == u:
        s += "A"
        return count_vowels(s, index + 1)
    else:
        return count_vowels(s, index+1)


def main():
    a = arrays.Array(5,0)
    res = linear_recursive(a, 0, 4)
    print(res)
    a[3] = 4
    print(a)
    res = linear_recursive(a, 0, 4)
    print(res)

    print(count_vowels("code commentary is useful", 0))
    print(count_vowels("thr3 b33 n0 vwls h33r3", 0))
    print(count_vowels("", 0))
    print(count_vowels("u", 0))
    
if __name__ == "__main__":
    main()
    