# Merge Two Sorted Strings Lexicographically

def merge(string1, string2) :
  # Base Case1
  if string1 == "" :
    if string2 == "" : 
      return ""
    return string2

  # Base Case2
  elif string2 == "" :
    return string1

  # Recursive Case1
  elif string1[0] > string2[0] :
      return string2[0] + merge(string1, string2[1:])

  # Recursive Case2
  return string1[0] + merge(string1[1:], string2)

# Driver Code
string1 = "acu"
string2 = "bst"
print(merge(string1, string2))