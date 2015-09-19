# Trying to split punctuation
neg_list=[]
pos_list=[]
with open('positive_words.txt','r+') as pos_words_file:
	
	for word in pos_words_file:
		word=word.lower()	#convert adjectives to lower case 
		pos_list.append(word[:len(word)-1])	#remove '/n'	
	
with open('negative_words.txt','r+') as neg_words_file:
	for word in neg_words_file:
		word=word.lower() 	#convert adjectives to lower case 
		neg_list.append(word[:len(word)-1])		#remove '/n'	
#print neg_list
#print pos_list

positive_count=0
negative_count=0
new_word_arr=[]
adj=[]
with open('input_file.txt','r+') as inputfile:
	for line in inputfile:
		word_arr=line.split()
		for word in word_arr:
			word=word.lower()
			word=list(word)
			i=0
			flag=0
			word_len=len(word)
			for char in word:
				i+=1
				if(char=='.'or char==','or char=='!' or char=='?'):
					flag=1
					#print char
					#print word
					new_word=word[:i-1]
					new_word=''.join(new_word)
					word=''.join(word)
					#print new_word
					new_word_arr.append(new_word)
					new_word_arr.append(char)
					del word_arr[word_arr.index(word)]
				if(i==word_len and flag==0):
					new_word_arr.append(''.join(word))

		#print "punctuation separation done for a line"
		word_arr=new_word_arr
		#print "word_arr=%s" % word_arr			
for word in word_arr:	
			if('not' in word_arr[-3]):
				if(word in pos_list):
					negative_count+=1
				if(word in neg_list):
					positive_count+=1
			
			else:	
				if(word in pos_list):
					positive_count+=1
				if(word in neg_list):
					negative_count+=1
			if(word in pos_list or word in neg_list):
				adj.append(word)	

if(positive_count>negative_count):
	print("positive")
elif(positive_count<negative_count):
	print("negative")
else:
	print("neutral")

print "neg count %d" % negative_count
print "pos count %d" % positive_count
#print word_arr
print "adjectives found are %s" %adj
