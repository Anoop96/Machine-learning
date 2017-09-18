from recommendation_data import dataset
import math
#print(dataset['Lisa Rose']['Lady in the Water'])

def similarity_score(person1 , person2):
	both_viewed = {}
# to get the rated movies by both of them.
	for item in dataset[person1]:
		if item in dataset[person2]:
			both_viewed[item] = 1

		# to check whether they have common rating item
		if len(both_viewed) == 0:
			return 0

		# finding euclidian distance since is not a very good approach so we are not using it here.
		sum_of_euclidian_distance  = []
		for item in dataset[person1]:
			if item in dataset[person2]:
				sum_of_euclidian_distance.append(pow(dataset[person1][item] - dataset[person2][item],2))
		sum_of_euclidian_distance = sum(sum_of_euclidian_distance)
		return 1/(1+math.sqrt(sum_of_euclidian_distance))

		# we use pearson correlation
		# Sxx = sum(x^2) - (sum(x^2))/n
		# Syy = sum(y^2) - (sum(y^2))/n
		# Sxy = sum(xy) - (sum(x))(sum(y))/n
		# r = Sxy/sqrt(Sxx*Syy)
def pearson_correlation(person1, person2):
	#to get both rated items
	both_rated = {}
from recommendation_data import dataset
import math
#print(dataset['Lisa Rose']['Lady in the Water'])

def similarity_score(person1 , person2):
	both_viewed = {}
# to get the rated movies by both of them.
	for item in dataset[person1]:
		if item in dataset[person2]:
			both_viewed[item] = 1

		# to check whether they have common rating item
		if len(both_viewed) == 0:
			return 0

		# finding euclidian distance since is not a very good approach so we are not using it here.
		sum_of_euclidian_distance  = []
		for item in dataset[person1]:
			if item in dataset[person2]:
				sum_of_euclidian_distance.append(pow(dataset[person1][item] - dataset[person2][item],2))
		sum_of_euclidian_distance = sum(sum_of_euclidian_distance)
		return 1/(1+math.sqrt(sum_of_euclidian_distance))

		# we use pearson correlation
		# Sxx = sum(x^2) - (sum(x^2))/n
		# Syy = sum(y^2) - (sum(y^2))/n
		# Sxy = sum(xy) - (sum(x))(sum(y))/n
		# r = Sxy/sqrt(Sxx*Syy)
def pearson_correlation(person1, person2):
	#to get both rated items
	both_rated = {}

	for item in dataset[person1]:
		if item in dataset[person2]:
			both_rated[item] = 1
	number_of_ratings = len(both_rated)

	#checking if they have common ratings
	if(number_of_ratings == 0):
		return 0
	#adding all the preferences of the users ->sum(X)
	person1_preferences_sum = sum([dataset[person1][item]for item in both_rated])
	person2_preferences_sum = sum([dataset[person2][item]for item in both_rated])

	#sum up the square of the all preferences of each users ->sum(X^2)
	person1_square_preferences_sum = sum([pow(dataset[person1][item],2) for item in both_rated])
	person2_square_preferences_sum = sum([pow(dataset[person2][item],2) for item in both_rated])

	#sum up the product value of both preferences of each item ->sum(X*Y)
	product_sum_of_both_user = sum([dataset[person1][item] * dataset[person2][item]for item in both_rated])

	#calculate the pearson similarity_score ->sum(X*Y) - (sum(X^2)*sum(Y^2)/no of ratings)
	numerator_value = product_sum_of_both_user - (person1_preferences_sum*person2_preferences_sum/number_of_ratings)
	# sqrt(( sum(X^2)- sum(X)^2 /no of ratings ) * (sum(Y^2) - sum(Y)^2 / no of ratings))
	denominator_value =math.sqrt((person1_square_preferences_sum - pow(person1_preferences_sum,2)/number_of_ratings)*(person2_square_preferences_sum - pow(person2_preferences_sum,2)/number_of_ratings))
	if denominator_value == 0:
		return 0;
	else:
		r = numerator_value/denominator_value
		return r
print("by pearson correlation")
print(pearson_correlation('Lisa Rose', 'Gene Seymour'))
print("by similarity_score")
print(similarity_score('Lisa Rose', 'Jack Matthews'))


def most_similar_users(person, number_of_users):
	#return similar users for a given specific person
	# for other_person in dataset:
	# 	if(other_person!=person):
	# 		scores.append(pearson_correlation(person ,other_person),other_person)
	scores = [(pearson_correlation(person,other_person),other_person) for other_person in dataset if  other_person != person ]
	scores.sort()
	scores.reverse()
	return scores[0:number_of_users]
print(most_similar_users('Lisa Rose',3))


def user_recommendations(person):
	# get recommendations for a persons by using a weighted avg of other_persons
	totals = {}
	simsums = {}
	ranking_list = []
	for other in dataset:
		#dont compare me to myself
		if other == person:
			continue
		sim = pearson_correlation(person,other)
		if sim <=0:
			#to ignore score 0 or lower
			continue
		for item in dataset[other]:
			#only score movie i havent seen yet
			if item not in dataset[person] or dataset[person][item] == 0:
				#similarity* scores
				totals.setdefault(item,0)
				totals[item] +=dataset[other][item]*sim
				#sum of similarities
				simsums.setdefault(item,0)
				simsums[item] += sim
#normalised list
	ranking = [(total/simsums[item],item) for item,total in totals.items()]
	ranking.sort()
	ranking.reverse()
	#return recommended items
	recommendation_list = [recommend_item for score,recommend_item in ranking]
	return recommendation_list

	for item in dataset[person1]:
		if item in dataset[person2]:
			both_rated[item] = 1
	number_of_ratings = len(both_rated)

	#checking if they have common ratings
	if(number_of_ratings == 0):
		return 0
	#adding all the preferences of the users ->sum(X)
	person1_preferences_sum = sum([dataset[person1][item]for item in both_rated])
	person2_preferences_sum = sum([dataset[person2][item]for item in both_rated])

	#sum up the square of the all preferences of each users ->sum(X^2)
	person1_square_preferences_sum = sum([pow(dataset[person1][item],2) for item in both_rated])
	person2_square_preferences_sum = sum([pow(dataset[person2][item],2) for item in both_rated])

	#sum up the product value of both preferences of each item ->sum(X*Y)
	product_sum_of_both_user = sum([dataset[person1][item] * dataset[person2][item]for item in both_rated])

	#calculate the pearson similarity_score ->sum(X*Y) - (sum(X^2)*sum(Y^2)/no of ratings)
	numerator_value = product_sum_of_both_user - (person1_preferences_sum*person2_preferences_sum/number_of_ratings)
	# sqrt(( sum(X^2)- sum(X)^2 /no of ratings ) * (sum(Y^2) - sum(Y)^2 / no of ratings))
	denominator_value =math.sqrt((person1_square_preferences_sum - pow(person1_preferences_sum,2)/number_of_ratings)*(person2_square_preferences_sum - pow(person2_preferences_sum,2)/number_of_ratings))
	if denominator_value == 0:
		return 0;
	else:
		r = numerator_value/denominator_value
		return r
print("by pearson correlation")
print(pearson_correlation('Lisa Rose', 'Gene Seymour'))
print("by similarity_score")
print(similarity_score('Lisa Rose', 'Jack Matthews'))


def most_similar_users(person, number_of_users):
	#return similar users for a given specific person
	# for other_person in dataset:
	# 	if(other_person!=person):
	# 		scores.append(pearson_correlation(person ,other_person),other_person)
	scores = [(pearson_correlation(person,other_person),other_person) for other_person in dataset if  other_person != person ]
	scores.sort()
	scores.reverse()
	return scores[0:number_of_users]
print(most_similar_users('Lisa Rose',3))


def user_recommendations(person):
	# get recommendations for a persons by using a weighted avg of other_persons
	totals = {}
	simsums = {}
	ranking_list = []
	for other in dataset:
		#dont compare me to myself
		if other == person:
			continue
		sim = pearson_correlation(person,other)
		if sim <=0:
			#to ignore score 0 or lower
			continue
		for item in dataset[other]:
			#only score movie i havent seen yet
			if item not in dataset[person] or dataset[person][item] == 0:
				#similarity* scores
				totals.setdefault(item,0)
				totals[item] +=dataset[other][item]*sim
				#sum of similarities
				simsums.setdefault(item,0)
				simsums[item] += sim
#normalised list
	ranking = [(total/simsums[item],item) for item,total in totals.items()]
	ranking.sort()
	ranking.reverse()
	#return recommended items
	recommendation_list = [recommend_item for score,recommend_item in ranking]
	return recommendation_list
