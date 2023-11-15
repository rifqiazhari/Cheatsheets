0. #Data Types
    Text type:		str
	Numeric type:	int, float, complex
	Sequence type:	list, tuple, range
	Mapping type:	dict
	Set types:		set, frozenset
	Boolean type:	bool
	Binary types:	bytes, bytearray, memoryview
	None type:		NoneType
1. #DF TYPES
    1.1 #?
        
    1.2 #HOW TO CREATE?
        1.2.1 List

            0.	type(var)	#to check variable types
            len(var)	#to count the lenght of a variable  
    1.3 #HOW TO ACCESS? Indexed, Unindexed, and Key_indexed

                print("Yes, 'key4' is one of the keys in the dict0 dictionary")
    1.4 #HOW TO UPDATE, ADD, OR REMOVE
        1.4.1 #HOW TO REPLACE/UPDATE? Changeable and Unchangeable
             dict0["brand"] = "Toyota"						result: {'brand': 'Toyota', 'model': 'Mustang'}							#update a new value within a key
                    dict0.update({"brand": Toyota})					result: {'brand': 'Toyota', 'model': 'Mustang'}							#update a new value within a key
        1.4.2 #HOW TO INSERT/ADD (+++) NEW ITEM?
                    dict0.update({"year": 1964})					result: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}				#add an item (key + value)
        1.4.3 #HOW TO REMOVE (---) ITEMS?
            1.4.3.1 List
        #HOW TO UPDATE, ADD, OR REMOVE COLUMNS OR ROWS
        #ADD
        ALTER TABLE df										#add column
			ADD column5 datatype;
		ALTER TABLE df
			ADD column5 datatype							#add column with same value
			DEFAULT 'values';
        #HOW TO DELETE
        ALTER TABLE df										#delete single column
			DROP COLUMN `column1`;
		ALTER TABLE df										#delete multiple columns
			DROP COLUMN `column1`,
			DROP COLUMN `column3`,
			DROP COLUMN `column4`;
        #HOW TO RENAME
    	ALTER TABLE df									#rename single column
			RENAME COLUMN `column1` to `column2`;
		ALTER TABLE df									#rename multiple columns
			RENAME COLUMN `column1` to `column4`,
			RENAME COLUMN `column2` to `column7`,
			RENAME COLUMN `column3` to `column9`;
 
   
4. #PREVIEW [SQL]
    4.1 #PREVIEW TABLE SUMMARY
        ?
    4.2 #PREVIEW TABLE
        ?
    4.3 #PREVIEW COLUMNS
        SELECT column1					single			column		by_column_label					#column_1 and column_2
			FROM df;
		SELECT column1, column2			multiple		columns		by_column_label					#column_1 and column_2
			FROM df;
		SELECT `column1`, `column2`		multiple		columns		by_column_label					#column_1 and column_2
			FROM df
    4.4 #PREVIEW ROWS OR COLUMNS WITH CONDITION    
        SELECT column1, column2
            FROM df;
        SELECT `column1`, `column2`
            FROM df
            WHERE condition;
        SELECT DISTINCT column1
            FROM df
            WHERE condition;
        SELECT column1, column2
            FROM df
            ORDER BY column1 ASC [DESC];
        SELECT column1, column2
            FROM df
            ORDER BY column1
            LIMIT n
            OFFSET offset;
        SELECT column1, aggregate(column2)
            FROM df
            GROUP BY column1;
        SELECT column1, aggregate(column2)
            FROM df
            GROUP BY column1
            HAVING condition;
        
        SELECT column1, column2
            FROM df
            INNER JOIN df2
            ON condition;
        SELECT column1, column2
            FROM df
            LEFT JOIN df2
            ON condition;
        SELECT column1, column2
            FROM df
            RIGHT JOIN df2
            ON condition;
        SELECT column1, column2
            FROM df
            FULL OUTER JOIN df2
            ON condition;
        SELECT column1, column2`
            FROM df
            CROSS JOIN df2;
        SELECT column1, column2`
            FROM df, df2
        SELECT column1, column2`
            FROM df A
            INNER JOIN df2 B condition;
        SELECT column1, column2`
            FROM df
            UNION [ALL]
            SELECT column1, column2`
            FROM df2
        SELECT column1, column2`
            FROM df
            INTERSECT
            SELECT column1, column2`
            FROM df2
        SELECT column1, column2`
            FROM df
            MINUS
            SELECT column1, column2`
            FROM df2
        SELECT column1, column2`
            FROM df
            WHERE column1 [NOT] LIKE pattern;
        SELECT column1, column2`
            FROM df
            WHERE column1 [NOT] IN values_list;
        SELECT column1, column2`
            FROM df
            WHERE column1 BETWEEN low AND high;
        SELECT column1, column2`
            FROM df
            WHERE column1 IS [NOT] NULL;

5. #JOIN & COMBINE [SQL]
    5.1 #JOIN        
        create table table12 (
            select table1.column1, `column2`, `column3` from table1
        inner join table2
        on table1.column1 = table2.column1
        );

6. #DATAFRAME MANIPULATION [SQL]
    6.1 #PIVOTING
        ?
    6.2 #NULL DETECTION
        select 'columnname'
            from df
            where 'columnname' is null      #IS NULL
        select 'columnname'
            from df
            where 'columnname' is not null  #NOT NULL
