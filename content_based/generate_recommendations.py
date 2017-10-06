import pickle, math, time

#Load Trained Model
with open('model.sav','rb') as mod:
	scores = pickle.load(mod)

#Load Data
with open('data.sav','rb') as data:
	herb_data = pickle.load(data)

#Generate recommendations
def sim_gen(user_vec,item_vec):
	recs=[]
	i=0
	for item in item_vec:
		A_dot_B=0
		if item == user_vec:
			i+=1
			continue
		for word in user_vec:
			if word in item:
				A_dot_B+=user_vec[word]*item[word]
		mod_A=math.sqrt(sum([x**2 for x in user_vec.values()]))
		mod_B=math.sqrt(sum([x**2 for x in item.values()]))
		recs.append(tuple([i,A_dot_B/(mod_A*mod_B)]))
		i+=1
	return sorted(recs, key=lambda x:x[1],reverse=True)[:10]


#Queries
query = input('Enter Query:').lower()
start = time.time()
user_vec=[]
print('\nRelated to '+query.capitalize()+':')
for i in herb_data:
	if query in i['botanical_name'].lower() or i['family'] == query:
		user_vec = scores[herb_data.index(i)]
		break
if not user_vec:
	index=0
	for i in herb_data:
		if query in str(i['properties']).lower() or query in str(i['places']).lower():
			if not user_vec:
				index=herb_data.index(i)
				user_vec = scores[index]
			print(i['botanical_name'])
	if user_vec:
		print('\nMore related to:'+str(herb_data[index]['botanical_name']))
		
if not user_vec:
	print('\nInvalid Input')
else:
	recs=sim_gen(user_vec,scores)
	for i in recs:
		print(herb_data[i[0]]['botanical_name'])
print('Results generated in: '+str(time.time()-start))