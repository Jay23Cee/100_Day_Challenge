sentence= "Happy World"

array_sen = list(sentence)

rev_array =[]
size = len(array_sen)-1

for x in range(len(array_sen)):
    rev_array.append(array_sen[size])
    size -=1

reverse_sentence=''.join(rev_array)

print(reverse_sentence)
