
# def compress(s):
#     output = ''
#     lst = []
#     dic = {}
#     for i in s:
#         if i not in dic:
#             dic[i] = 1
#         else:
#             dic[i] = dic[i] + 1
#     for k,v in dic.items():
#         lst += str(v), k
#     for i in lst:
#         if i == '1':
#             continue
#         else:
#             output  += i
    
#     return output




def compress(s):
    i = 0
    j = 0
    k = 1 
    result = []
    c = s + 'a'
    output = ''
    while k < len(c):
        if c[j] == c[k]:
            j += 1
            k += 1
        else:
            num = str(len(c[i:k]))
            result += num, c[j]
            k += 1
            j += 1
            i = j
    for i in result:
        if i =='1':
            continue
        output += i
    return output

print(compress('ppoppppp'))

## Better Method

def compress(s):
  s += '!'
  result = []
  i = 0
  j = 0
  while j < len(s):
    if s[i] == s[j]:
      j += 1  
    else:
      num = j - i
      if num == 1:
        result.append(s[i])
      else:
        result.append(str(num)) 
        result.append(s[i])
      i = j
    
  return ''.join(result)


   # n = length of string
    #Time: O(n)
    #Space: O(n)








