
neg_list=[]
pos_list=[]
neg_found=[]
pos_found=[]
with open('positive_words.txt','r+') as pos_words_file:
	
	for word in pos_words_file:
		word=word.lower()	#convert adjectives to lower case 
		pos_list.append(word[:len(word)-1])	#remove '\n'	
	
with open('negative_words.txt','r+') as neg_words_file:
	for word in neg_words_file:
		word=word.lower() 	#convert adjectives to lower case 
		neg_list.append(word[:len(word)-1])		#remove '\n'	
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
				if(char=='.'or char==','or char=='!' or char=='?'or char==';' or char==":"):
					flag=1
					new_word=word[:i-1]
					new_word=''.join(new_word)
					
					new_word_arr.append(new_word)
					new_word_arr.append(char)
					
				if(i==word_len and flag==0):
					new_word_arr.append(''.join(word))

		# "punctuation separation done for a line"
		word_arr=new_word_arr
	print "word_arr=%s" % word_arr			
for word in word_arr:	
			if(word=='not'): 
				cur_index=word_arr.index(word)
				print cur_index
				cur_index+=1
				while True:
					if((word_arr[cur_index]  in neg_list) or (word_arr[cur_index]  in pos_list) or (word_arr[cur_index] =='.') or cur_index==word_arr.length+1):
						break
					else:
						cur_index+=1
						print cur_index
									
								
				if(word_arr[cur_index] in pos_list):
						neg_found.append('not')
						neg_found.append(word_arr[cur_index])
						negative_count+=1
				if(word_arr[cur_index] in neg_list):
						pos_found.append('not')
						pos_found.append(word_arr[cur_index])
						positive_count+=1
				del word_arr[word_arr.index('not')]
				del word_arr[cur_index]
			
			else:	
				if(word in pos_list):
					pos_found.append(word)
					positive_count+=1
				if(word in neg_list):
					neg_found.append(word)
					negative_count+=1
			
if(positive_count>negative_count):
	print("positive")
elif(positive_count<negative_count):
	print("negative")
else:
	print("neutral")

print "neg count %d" % negative_count
print "pos count %d" % positive_count
#print word_arr
print "pos adjectives found are %s" %pos_found
print "neg adjectives found are %s" %neg_found
