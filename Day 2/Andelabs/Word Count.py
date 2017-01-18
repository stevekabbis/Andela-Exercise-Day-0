def words(a):  #define variable with an argument
  b=a.split()
  split_words=[] # where the dictionary will be 
  
  for x in b:
    try:
      x2=int(x)
      split_words.append(x2)
    except:
      split_words.append(x)
        
  words_dict = {x:split_words.count(x) for x in split_words}
  return words_dict

a = "battlefield 4 1 battlefield 4 1"
print (words(a))
b = "battlefield four one battlefield four 1"
print (words(b))
