1. #Variable (Single Item) Types
    1.1 #DATA TYPES in Python
        Text type:		str
        Numeric type:	int, float, complex
        Sequence type:	list, tuple, range
        Mapping type:	dict
        Set types:		set, frozenset
        Boolean type:	bool
        Binary types:	bytes, bytearray, memoryview
        None type:		NoneType
    1.2 #HOW TO CREATE VARIABLE  (Single Item)?
        var = "Abcd"									#for string
        var = 123										#for integer
        var = 123.5										#for float
        var = 3+2j										#for complex
        var = ["apple", "banana", "cherry"]				#for list
        var = ("apple", "banana", "cherry")				#for tuple	
        var = range(6)									#for range	
        var = {"name" : "John", "age" : 36}				#for dict
        var = {"apple", "banana", "cherry"}				#for set
        var = frozenset({"apple", "banana", "cherry"})	#for frozenset	
        var = True										#for bool	
        var = b"Hello"									#for bytes	
        var = bytearray(5)								#for bytearray	
        var = memoryview(bytes(5))						#for memoryview	
        var = None										#for NoneType
                                                        rules:
                                                        - A variable name must start with a letter or the underscore character
                                                        - A variable name cannot start with a number
                                                        - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
                                                        - Variable names are case-sensitive (age, Age and AGE are three different variables)
                                                        - A variable name cannot be any of the Python keywords.
        var1, var2, var3 = "Abcd", "Efgh", "Hijk"		#for multiple variables
        var1 = var2 = var3 = "Abcd"						#for same values multiple variables

0. #Variable (Multiple Items) Types
    1.1 #DATA COLLECTION TYPES
	List, Tuple, Set, and Dictionary are used to store multiple items in a single variable
	
	List is a collection which is			ordered		changeable		indexed			Allows duplicate members.
	Tuple is a collection which is			ordered		unchangeable*	indexed			Allows duplicate members.
	Set is a collection which is			unordered	unchangeable**	unindexed		No duplicate members.
	Dictionary is a collection which is		ordered***	changeable		key_indexed		No duplicate members.
				
		* = can't update, remove, or add
		** = can add or remove, can't update
				
			Indexability:
					- Indexed means that the first item has index [0], the second item has index [1] etc
						- Since list and tuple are indexed, they can have items with the same value
					- Key_indexed means that we used the key as an index
				- Ordered means that the items have a defined order, and that order will not change
					If you add new items to a list and tuple, the new items will be placed at the end.
				- Unordered means that the items do not have a defined order
					- Items can appear in a different order every time you use them, and cannot be referred to by index or key
				- Changeable means that we can change, add, and remove items in a list after it has been created.
				- Unchangeable
					- In tuple, Unchangeable means that we cannot change, add or remove items after the tuple has been created
					- In set, Unchangeable means that we cannot change the items after the set has been created
						- Set items are unchangeable, but you can remove items and add new items
				- Duplicate
					- Indexed variables can have duplicate values
					- Unindexed variables cannot have two items with the same value.
						- In set, The values True and 1 are considered the same value, and are treated as duplicates
					- In dictionary, since they used key_indexed we are not allowed to have duplicate keys               
    1.2 #HOW TO CREATE?
        1.2.1 List
            list0 = ["Abcd", "Efgh", "Hijk"]								result: ['Abcd', 'Efgh', 'Hijk']
            list0 = list(("Abcd", "Efgh", "Hijk"))							#list()
            list0 = ["apple", "banana", "cherry", "apple", "cherry"]		#allow duplicates
            list1 = ["apple", "banana", "cherry"]							#list with string dt
            list2 = [1, 5, 7, 9, 3]											#list with int dt
            list3 = [True, False, False]									#list with boolean dt
            list1 = ["abc", 34, True, 40, "male"]							#list with multiple dt
        1.2.2 Tuple
            tuple0 = ("Abcd", "Efgh", "Hijk")								result: ('Abcd', 'Efgh', 'Hijk')
            tuple0 = tuple(("Abcd", "Efgh", "Hijk"))						#tuple()
            tuple0 = ("Abcd",)												#tuple with single value
            tuple0 = ("Abcd")												#a string, not a tuple
            tuple1 = ("apple", "banana", "cherry")							#tuple with string dt
            tuple2 = (1, 5, 7, 9, 3)										#tuple with int	dt
            tuple3 = (True, False, False)									#tuple with boolean dt
            tuple1 = ("abc", 34, True, 40, "male")							#tuple with multiple dt
        1.2.3 Set
            set0 = {"Abcd", "Efgh", "Hijk"}									result: {'Abcd', 'Efgh', 'Hijk'}
            set0 = set(("Abcd", "Efgh", "Hijk"))							#set()
            set1 = {"apple", "banana", "cherry"}							#set with string dt
            set2 = {1, 5, 7, 9, 3}											#set with int dt
            set3 = {True, False, False}										#set with boolean dt
            set1 = {"abc", 34, True, 40, "male"}							#set with multiple dt
        1.2.4 Dictionary
            dict0 = {"Brand": "Abcd", "Model": "Efgh", "Year": "Hijk"}		result: {'Brand': 'Abcd', 'Model': 'Efgh', 'Year': 'Hijk'}
            dict0 = dict(Brand= "Abcd", Model= "Efgh", Year= "Hijk")		#dict()
            thisdict = {													#dict with multiple dt
                "brand": "Ford",
                "electric": False,
                "year": 1964,
                "colors": ["red", "white", "blue"]
                }

            0.	type(var)	#to check variable types
            len(var)	#to count the lenght of a variable  
    1.3 #HOW TO ACCESS? Indexed, Unindexed, and Key_indexed
        1.3.1 List & Tuple
            list[0]		or	tuple[0]								#to access with index
            list[-2]	or	tuple[-2]								#to access with negative index (-2 = second from the back)
            list[1:3]	or	tuple[1:3]								#to access with a range of index (1 included, 3 not included)
            list[:2]	or	tuple[:2]								#to access with a range that start from the beginning (2 not included)
            list[2:]	or	tuple[2:]								#to access with a range that start from selected number and goes to the end (2 included)
            list[-3:-1]	or	tuple[-3:-1]							#to access with a range of negative index (-1 not included)
            if "Abcd" in list:										#check if item exists with condition (we can do the same with tuple)
                print("Yes")
        1.3.2 Dictionary
            dict0["key0"]											#get value from key0
            dict0.get("key0")										#get value from key0
            dict0.keys()											#return the keys
            dict.values()											#return the values
            dict.items()											#return the keys and values as tuples

            if "key4" in dict0:										#check if the key exists
                print("Yes, 'key4' is one of the keys in the dict0 dictionary")
    1.4 #HOW TO UPDATE, ADD, OR REMOVE ITEM
        1.4.1 #HOW TO REPLACE/UPDATE? Changeable and Unchangeable
            1.4.1.1 List
                list0 = ["apple", "banana", "cherry"]
                    list0[1]	= "blackcurrant"					result: ['apple', 'blackcurrant', 'cherry']								#change single item value
                    list0[1:3]	= ["blackcurrant", "watermelon"]	result: ['apple', 'blackcurrant', 'watermelon']							#change multiple item value
                    list0[1:2]	= ["blackcurrant", "watermelon"]	result: ['apple', 'blackcurrant', 'watermelon', "cherry"]				#change single item with two values
                    list0[1:3]	= ["blackcurrant"]					result: ['apple', 'blackcurrant', 'blackcurrant']						#change multiple item with one value
            1.4.1.2 Tuple & Set
                %since it unchangable, we must convert to list to replace/update and change it back
                list0 = list(tuple0)	or	list0 = list(set0)
                tuple0 = tuple(list0)	or	set0 = set(list0)
            1.4.1.3 Dictionary
                dict0 = {"brand": "Ford", "model": "Mustang"}		result: {'brand': 'Ford', 'model': 'Mustang'}
                    dict0["brand"] = "Toyota"						result: {'brand': 'Toyota', 'model': 'Mustang'}							#update a new value within a key
                    dict0.update({"brand": Toyota})					result: {'brand': 'Toyota', 'model': 'Mustang'}							#update a new value within a key
        1.4.2 #HOW TO INSERT/ADD (+++) NEW ITEM?
            1.4.2.1 List
                list0 = ["apple", "banana", "cherry"]
                    list0.insert(2, "watermelon")					result: ['apple', 'banana', 'watermelon', 'cherry']						#add a new value to index [2]	
                    list0.append("orange")							result: ['apple', 'banana', 'cherry', 'orange']							#add a new value to the last index					
                list0 = ["apple", "banana", "cherry"]
                list1 = ["mango", "pineapple", "papaya"]
                    list0.extend(list1)								result: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']	#combine the second to the first
                list0 = ["apple", "banana", "cherry"]
                tuple0 = ("mango", "pineapple", "papaya")
                    list0.extend(tuple0)							result: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']	#combine the second to the first
            1.4.2.2 Tuple	
                tuple0 = ("apple", "banana", "cherry")
                tuple1 = ("orange",)
                    tuple0 += tuple1								result: tuple0 = ("apple", "banana", "cherry", "orange")				#combine the second to the first
            1.4.2.3 Set
                set0 = {"apple", "banana", "cherry"}
                    set0.add("orange")								result: {'orange', 'apple', 'banana', 'cherry'}							#add a new value
                set1 = {"pineapple", "mango", "papaya"}
                    set0.update(set1)								result: {'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}	#combine the second to the first
                list0 = ["kiwi", "orange"]
                    set0.update(list0)								result: {'banana', 'cherry', 'apple', 'orange', 'kiwi'}					#update() can be use in list, tuple, dictionary, and set
            1.4.2.4 Dictionary
                dict0 = {"brand": "Ford", "model": "Mustang"}		result: {'brand': 'Ford', 'model': 'Mustang'}
                    dict0["year"] = "1964"							result: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}				#add an item (key + value)
                    dict0.update({"year": 1964})					result: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}				#add an item (key + value)
        1.4.3 #HOW TO REMOVE (---) ITEMS?
            1.4.3.1 List
                list0 = ["apple", "banana", "cherry"]					result: ['apple', 'banana', 'cherry']
                    list0.remove("banana")								result: ['apple', 'cherry']												#remove item
                    list0.pop(1)										result: ['apple', 'cherry']												#remove item at index [1]
                    list0.pop()											result: ['apple', 'banana']												#remove item at the last index
                    list0.clear()										result: []																#remove entire items
                    del list0[1]										result: ['apple', 'cherry']												#remove item at index [1]
                    del list0											result: 																#delete the list
            1.4.3.2 Tuple
                %for tuple, since it unchangable, we must convert to list to remove and change it back to tuple
                %tuple can't removed, only deleted
                list0 = list(tuple0)
                tuple0 = tuple(list0)
                    del tuple0											result:																	#delete the tuple
            1.4.3.3 Set
                set0 = {"apple", "banana", "cherry"}
                    set0.remove("banana")								result: {'apple', 'cherry'}												#remove item
                    set0.discard("banana")								result: {'apple', 'cherry'}												#remove item
                    set0.clear()										result: {}																#remove entire items
                    del set0											result:																	#delete the set
            1.4.3.4 Dictionary
                dict0 = {"brand": "Ford", "model": "Mustang"}			result: {'brand': 'Ford', 'model': 'Mustang'}
                    dict0.pop("brand")									result: {'model': 'Mustang'}											#remove item (key + value)
                    dict0.popitem()										result: {'brand': 'Ford'}												#remove item (key + value) at the last
                    dict0.clear()										result: {}																#remove entire items
                    del dict0["brand"]									result: {'model': 'Mustang'}											#remove item (key + value)
                    del dict0											result:																	#delete entire dictionary
    1.5 #HOW TO UNPACK? (Tuple to List/Str)
        1.5.1 Tuple
                tuple0 = ("apple", "banana", "cherry")
                    (green, yellow, red) = tuple0
                        print(green)		result: apple										#str
                        print(yellow)		result: banana										#str
                        print(red)			result: cherry										#str

                tuple1 = ("apple", "banana", "cherry", "strawberry", "raspberry")
                    (green, yellow, red*) = tuple1
                        print(green)		result: apple										#str
                        print(yellow)		result: banana										#str
                        print(red)			result: ['cherry', 'strawberry', 'raspberry']		#list
                
                tuple1 = ("apple", "banana", "cherry", "strawberry", "raspberry")
                    (green, yellow*, red) = tuple1
                        print(green)		result: apple										#str
                        print(yellow)		result: ['banana', 'cherry', 'strawberry']			#list
                        print(red)			result: raspberry									#str
    1.6 #HOW TO LOOP? (list0 = ["apple", "banana", "cherry"])
            1.4.5.1 List & Tuple & Set
            -	for x in list0:								#for loop (list, tuple, set)
                    print(x)
            -	[print(x) for x in list0]					#for loop (shortest) (list, tuple, set)
            1.4.5.2 List & Tuple
                -	for i in range(len(list0)):				#for loop (list, tuple)
                        print(list0[i])
                -	i=0										#while loop (list, tuple)
                    while i < len(list0):
                        print(list0[i])
                        i = i + 1
            1.4.5.3 Dictionary
                -	for x in dict0:							#return values, use index
                        print(dict[x])
                -	for x in dict0.values():				#return values
                        print(x)
                -	for x in dict0.keys():					#return keys
                        print(x)
                -	for x, y in dict0.items():				#return items (keys + values)
                        print(x, y)
    1.7 #COMPREHENSION
            list0 = ["apple", "banana", "cherry", "kiwi", "mango"]
            list1 = []
                for x in list0:												result:	['apple', 'banana', 'mango']							#if condition
                    if "a" in x:
                        list1.append(x)
                %from list/tuple/set to list/set
                list1 = [x for x in list0 if "a" in x]						result:	['apple', 'banana', 'mango']							#if condition, list to list
                set1 = {x for x in list0 if "a" in x}						result:	{'apple', 'banana', 'mango'}							#if condition, list to set
                list1 = [x for x in list0 if x != "apple"]					result: ['banana', 'cherry', 'kiwi', 'mango']					#if condition
                list1 = [x.upper() for x in list0]							result: ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']			#return capitalize version
                list1 = [x if x != "banana" else "orange" for x in list0]	result: ['apple', 'orange', 'cherry', 'kiwi', 'mango']			#if condition
                list2 = [x for x in range(10)]								result: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                list2 = [x for x in range(10) if x < 5]						result: [0, 1, 2, 3, 4]

 1.8 #HOW TO UPDATE, ADD, OR REMOVE COLUMNS OR ROWS
        #ADD

        #HOW TO DELETE
        df.drop(0, axis=0)									#delete single row
		df.drop([2,5], axis=0)								#delete multiple rows
		df.drop('title5', axis=1)							#delete column
		df.drop(['title5','title8'], axis=1]				#delete multiple columns
		df.drop(index=[2,5], columns=['title5','title8'])	#delete both rows and columns (single, multiple)
        #HOW TO RENAME
    	df.rename(columns={'title1':'title5', 'title2':'title6'})	#rename columns (single, multiple)
		df.rename(index={0:'label1', 1:'label2'})					#rename rows (single, multiple)

     
3. #DATAFRAMES
    3.0 #CREATE SERIES (Dataframe with Single-Column )
    	- A Pandas Series is like a column in a table.
        - It is a one-dimensional array holding data of any type
        list0 = [1, 7, 2]
            series0 = pd.Series(a)									#series is labelled by int (automatically)
                result:
                0    1
                1    7
                2    2
            series0 = pd.Series(a, index = ["x", "y", "z"])			#series is labelled by custom from list
                result:
                x    1
                y    7
                z    2
        dict0 = {"day1": 420, "day2": 380, "day3": 390}				#series is labelled by custom from dictionary
            series1 = pd.Series(dict0)
                result:
                day1	420
                day2	380
                day3	390
            series1 = pd.Series(dict0, index ["day1", "day2"])		#series is labelled by custom from dictionary + filter
                result:
                day1	420
                day2	380
        - 0,1,2		x,y,z		day1,day2,day3		are called labels
    3.1 #CREATE DATAFRAME (Dataframe with Multi-Columns)
        - Datasets in Pandas are usually multi-dimensional tables, called DataFrames.
        - Series is like a column, a DataFrame is the whole table.
		dict0 = {
		  'cars': ["BMW", "Volvo", "Ford"],
		  'passings': [3, 7, 2]
		}
		df0 = pd.DataFrame(dict0)										#dataframe is labelled by int (automatically)
			result:
				cars	passings
			0	BMW		3
			1	Volvo	7
			2	Ford	2
		data = {
			"calories": [420, 380, 390],
			"duration": [50, 40, 45]
		}
		df1 = pd.DataFrame(data, index = ["day1", "day2", "day3"])		#dataframe is labelled by custom from list
			result:
					calories	duration
			day1	BMW			3
			day2	Volvo		7
			day3	Ford		2
            
        df = pd.DataFrame(
            {	"a": [4,5,6],
                "b": [7,8,9],
                "c": [10,11,12],
                index= [1,2,3])}
        df = pd.DataFrame(
            [	[4,5,6],
                [7,8,9],
                [10,11,12]],
                index= [1,2,3],
                columns=['a', 'b', 'c'])
    3.2 #IMPORT DATAFRAME
        df = pd.read_excel('file.xlsx')
        df = pd.read_csv('file.csv')

4. #PREVIEW [PYTHON]
    4.1 #PREVIEW TABLE SUMMARY
        df.info             #show dimension, first 5 rows, last 5 rows
        df.shape            #show dimension / number of columns and rows
        len(df.columns)		#show number of columns
		len(df)		        #show number of rows
        df.size             #show number of elements
    4.2 #PREVIEW TABLE
        df							#show 5 first & 5 last rows
		df.to_string()				#show all rows
		df.head()					#show 5 first rows
		df.head(n)					#show n first rows
		df.tail()					#show 5 last rows
		df.tail(n)					#show n last rows
		df.sample()					#show 1 random row
		df.sample(n)				#show n random rows
		df.shape					#show dataframe dimension
    4.3 #PREVIEW ROWS OR COLUMNS
        df.loc[0,:]						single			row			by_row_label_default			#label starts at 0
		df.loc[[2,5],:]					multiple		rows		by_row_label_default
		df.loc[2:5,:]					range			rows		by_row_label_default
		df.loc[2:5:2,:]					range+incr		rows		by_row_label_default
		df.loc["label7",:]				single			row			by_row_label					#label = row_name
		df.loc[["label7","label9"],:]	multiple		rows		by_row_label
		df.loc["label7":"label9",:]		range			rows		by_row_label
		df.loc["label7":"label9":2,:]	range+incr		rows		by_row_label
		df.loc[:,0]						single			column		by_column_label_default			#title starts at 0
		df.loc[:,[2,5]]					multiple		columns		by_column_label_default
		df.loc[:,2:5]					range			columns		by_column_label_default
		df.loc[:,2:5:2]					range+incr		columns		by_column_label_default
		df.loc[:,"title1"]				single			column		by_column_label					#key/title = column_label	#output = series
		df.loc[:,["title1","title5"]]	multiple		columns		by_column_label
		df.loc[:,"title1":"title5"]		range 			columns		by_column_label
		df.loc[:,"title1":"title5":2]]	range+incr		columns		by_column_label
		df.iloc[0,:]					single			row			by_row_index					#index starts at 0
		df.iloc[[2,5],:]				multiple		rows		by_row_index
		df.iloc[2:5,:]					range			rows		by_row_index
		df.iloc[2:5:2,:]				range+incr		rows		by_row_index
		df.iloc[:,0]					single			columns		by_column_index					#index starts at 0
		df.iloc[:,[2,5]]				multiple		columns		by_column_index
		df.iloc[:,2:5]					range			columns		by_column_index
		df.iloc[:,2:5:2]				range+incr		columns		by_column_index
		df.column1						single			column		by_column_label					#output = series
		df['column1']					single			column		by_column_label					#output = series		#column's name with space. 
		df[['column1','column2']]		multiple		columns 	by_column_label
		df.loc[:,["title1","title5"]]	multiple		columns		by_column_label					#new column's order
		df[['column2','column1']]		multiple		columns		by_column_label					#new column's order
		df.filter(items=[3,5],			like=None,		regex=None, axis=0)		by_row_label
		df.filter(items=['col1','col2'],like=None,		regex=None, axis=1)		by_column_label
		df.filter(items=None,			like='row2',	regex=None, axis=0)		by_row_label_pattern
		df.filter(items=None,			like='column2',	regex=None, axis=1)		by_column_label_pattern
    4.4 #PREVIEW ROWS AND COLUMNS
        df.loc[1, 'column1']					single		by_row_index & by_column_index		single		#1 in column_1
		df.loc[2:5, 'column1']					multiple	by_row_index & by_column_index		columns		#2 to 5 in column_1
		df.loc[2:5, ['column1', 'column3']]		multiple	by_row_index & by_column_index		columns		#2 to 5 in column_1 & column_3
		df.loc[[2,5], 'column1']				multiple	by_row_index & by_column_index		columns		#2 and 5 in column_1
		df.loc[[2,5], ['column1', 'column3']]	multiple	by_row_index & by_column_index		columns		#2 and 5 in column_1 & column_3
    4.5 #PREVIEW ROWS OR COLUMNS WITH CONDITION
        df.query('column1 > 7')					#by_column_label	
		df.loc[df.column1 < 5]					#by_column_label	#column_1 < 5
		df.loc[df.column1 > 5]					#by_column_label	#column_1 > 5
		df.loc[df.column1 == 5]					#by_column_label	#column_1 == 5
		df.loc[df.column1 <= 5]					#by_column_label	#column_1 <= 5
		df.loc[df.column1 >= 5]					#by_column_label	#column_1 >= 5
		df.loc[df.column1 < 5, 'column3']		#by_column_label	#column_3 when column_1 < 5
		df.loc[df['column1'] < 5]				#by_column_label	#column_1 < 5
		df.loc[df['column1'] < 5, 'column3']	#by_column_label	#column_3 when column_1 < 5
		
		df.['column4'].loc[lambda x: x > 2.1]	#by label with boolean
		df.index = [i for i in range(0,750,5)]	#0 to 750 with 5 increment
		df.iloc[:10]							#shows only the first 10 data
		df.iloc[:, 1].head(6)					#print the first 6 data of column [1]
		df.iloc[1:7, 2]							#print 1 to 7 of column [2]
		df.query('B > C & C < 4*D')				#print only data that match the boolean
		df.query('A in [5.7, 5.9]')				#check A if A is in 5.7 or 5.9
		df.query('A != [5.7, 5.9]')				#check A if A is not in 5.7 or 5.9
      

9. #SORT [PYTHON]
	list0 = ["orange", "mango", "kiwi", "pineapple", "banana"]
	list1 = [100, 50, 65, 82, 23]
		list0.sort()				#ascending
		list1.sort()				#ascending
		list0.sort(reverse = True)	#descending
		list0.reverse()				#reversing
	def myfunc(n):					#sorting with our own function
		return abs(n - 50)
	list1 = [100, 50, 65, 82, 23]
		list1.sort(key = myfunc)
	list3 = ["Orange", "mango", "Kiwi", "pineapple", "banana"]
		list3.sort()				#ascending (case-sensitive, capital going first)
		list3.sort(key = str.lower)	#ascending (to hande case-sensitive)
 
 
5. #JOIN & COMBINE [PYTHON]
    5.1 #JOIN
        pd.merge(df, df2, on='column1', how='left')
        pd.merge(df, df2, on='column1', how='right')
        pd.merge(df, df2, on='column1', how='inner')
        pd.merge(df, df2, on='column1', how='outer')
    5.2 #COMBINE
        pd.concat([df1, df2])
        pd.concat([df1, df2], axis=1)

6. #DATAFRAME MANIPULATION [PYTHON]
    6.1 #PIVOTING
        pd.pivot(df, var_name='column1', value_name='newcolumn2')
        pd.melt(df, id_vars='column1', value_name='newcolumn2', var_name='newcolumn3')
    6.2 #NULL DETECTION 
        df[df['columnname'].isna()]         #IS NULL
        df = df[~df['columnname'].isna()]   #NOT NULL

8. #Visualization [PYTHON]    
    8.1 #1 Variable
        8.1.1 #Continous Data [Histogram, Density]
            plt.hist(df.columnname, bins=20, rwidth=0.8)                            #Histogram, Range/20 Interval/Binwidth
            plt.xlabel('columnname')
            plt.ylabel('count')
            plt.show()
        
            rng = np.arange(df.columnname.min(), df.columnname.max(), 0.1)          #Density Plot, 0.1    
            plt.plot(rng, norm.pdf(rng, df.columnname.mean(), df.columnname.std()))
        8.1.2 #Discrete Data [Bar chart]
            plt.bar(courses, values, color ='maroon', width = 0.4)
            plt.xlabel("Courses offered")
            plt.ylabel("No. of students enrolled")
            plt.title("Students enrolled in different courses")
            plt.show()
            
    8.2 #2 Variable
        8.2.1 #Continous Data [Scatter Plot] 
            plt.scatter(x, y, c ="blue")            #(1)
            plt.show()
               
            plt.scatter(x1, y1, c ="pink",          #(2)
                linewidths = 2, 
                marker ="s", 
                edgecolor ="green", 
                s = 50)
     
                plt.xlabel("X-axis")
                plt.ylabel("Y-axis")
                plt.show() 
       8.2.2  #Discrete Data [Grouped Bar Chart, Stacked Bar Chart]
                
          

     
     
     
    
    
    
    
    #CORRELATION COEFFICIENT R
        cor(x, y)
    #CORRELATION COEFFICIENT Py
        np.corrcoef(x,y)                    #numpy
        scipy.stats.pearsonr(x, y)[0]       #scipy
        scipy.stats.spearmanr(x, y)[0]
        scipy.stats.kendalltau(x, y)[0]
        x.corr(y)                           #pandas
        y.corr(x)
        x.corr(y, method='spearman')
        x.corr(y, method='kendall')
    
    #BOXPLOT PY
        df.boxplot(column='columnname')
    
    #MIN, 25%, MEAN, MED, 75%, MAX R
        quantile(x)                         #MIN, 25%, MED, 75%, MAX
        mean(x)                             #MEAN
        min(x)                              #MIN
        median(x)                           #MED
        max(x)                              #MAX
        IQR(x)                              #75%-25% (Inter-Quartile Range (IQR))
    
    #MIN, 25%, MEAN, MED, 75%, MAX
        df['columnname'].describe()         #ALL
        df.columnname.describe()            #ALL
        np.mean(df.columnname)              #MEAN
        np.percentile(df.columnname, 0)     #MIN
        np.percentile(df.columnname, 25)    #25%
        np.percentile(df.columnname, 50)    #MED
        np.percentile(df.columnname, 75)    #75%
        np.percentile(df.columnname, 100)   #MAX
