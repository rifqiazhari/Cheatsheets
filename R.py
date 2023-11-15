1. #Data Types
    1.1 #DATA TYPES in R
        Text type:		character
        Numeric type:	numeric, integer, complex
        Boolean type:	logical
        Binary types:	raw bytes
    1.2 #HOW TO CREATE VARIABLE?
        var <- "Abcd"									#for character (using '<-')
        var = "Abcd"									#for character (using '=')
        var = 123										#for numeric
        var = 123L										#for integer
        var = 123.5										#for numeric
        var = 3+2i										#for complex
        var = TRUE										#for logical(boolean)
        var = charToRaw("Welcome")						#for charToRaw() - converts character data to raw data
        var = rawToChar("Welcome")						#for rawToChar() - converts raw data to character data
    #CREATE DATAFRAMES
    #IMPORT DATAFRAMES
    df <- read_csv('file.csv')
2. #Variable TYPES
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

                    'Ford', 'model': 'Mustang', 'year': 1964}				#add an item (key + value)
        1.4.3 #HOW TO REMOVE (---) ITEMS?
            1.4.3.1 List
 
 #HOW TO UPDATE, ADD, OR REMOVE COLUMNS OR ROWS
        #ADD
        rbind(df, c(column1, column2, column3))				#add row
        cbind(df, title5 = c(row1, row2, row3))				#add column
        df %>%												#add row
            rbind(list1)
        df %>%												#add column
            cbind(list1)
        #HOW TO DELETE
		df[-c(1),]											#delete single row
		df[-c(2,5),]										#delete multiple rows
		df[-c(2:5),]										#delete range rows
		df[,-c(1)]											#delete column
		df[,-c(2,5)]										#delete multiple colums
		df[,-c(2:5)]										#delete range columns
		df[-c(2:5),-c(1:3)]									#delete both rows and columns (single, multiple, range)
        #HOW TO RENAME
        df %>%
			setNames(c("column1", "column2"))						#rename columns (single, multiple)
            
4. #PREVIEW [R]
    4.1 #PREVIEW TABLE SUMMARY
        dim(df)			    #show dimension / number of columns and rows
		ncol(df)		    #show number of columns
		nrow(df)		    #show number of rows
		length(df)	 	    #show number of columns
    4.2 #PREVIEW TABLE
        head(df)					#show 6 first rows
		head(df, n)					#show n first rows
		tail(df)					#show 6 last rows
		tail(df, n)					#show n last rows
		str(df)						#show dataframe dimension
    4.3 #PREVIEW ROWS OR COLUMNS
        df$column1						single			column		by_column_label
		df[,"title1"]					single			column		by_column_label
		df[,c("title1","title5")]		multiple		columns		by_column_label
		df[1,]							single			row			by_row_index					#index starts at 1
		df[c(2,5),]						multiple		rows		by_row_index
		df[c(2:5),]						range			rows		by_row_index
		df[,1]							single			column		by_column_index					#column_index starts at 1
		df[,c(2,5)]						multiple		columns		by_column_index					#column_index starts at 1
		df[,c(2:5)] 					range			columns		by_column_index					#column_index starts at 1

            
5. #JOIN & COMBINE [R]
    5.1 #JOIN
        df %>%
            left_join(df2, by="column1")
        df %>%
            right_join(df2, by="column1")
        df %>%
            inner_join(df2, by="column1")
        df %>%
            full_join(df2, by="column1")
    5.2 #COMBINE
        rbind(df1,df2,df3)	#combine dfs vertically
        cbind(df1,df2,df3)	#combine dfs horizontally

6. #DATAFRAME MANIPULATION [R]
    6.1 #PIVOTING
        df %>%
            pivot_longer(!column1, names_to = "newcolumn2", values_to = "newcolumn3")
        df %>%
            pivot_wider(names_from = "columncolumn", values = "valuescolumn"
    6.2 #NULL DETECTION & FILTER 
               
8. #Visualization [R]   
    8.1 #1 Variable
        8.1.1 #Continous Data [Histogram, Density]    
            heights %>%                                                              #Histogram, 1value Interval/Binwidth
                filter(sex == "Female") %>% 
                ggplot(aes(height)) +
                geom_histogram(binwidth = 1, fill = "blue", col = "black") +
                xlab("Male heights in inches") +
                ggtitle("Histogram")
    
            heights %>%                                                              #Density Plot
                filter(sex == "Female") %>%
                ggplot(aes(height)) +
                geom_density(fill="blue")
    8.2 #2 Variable
        8.2.1 #Continous Data [Scatter Plot] 
            p <- df %>% ggplot() +                                              #Scatter Plot
                geom_point(aes(x=columnname1, y=columnname2, label=columnname3))
            
            p + geom_point(size = 3, color='blue') +                            #Scatter Points Size
                geom_text(nudge_x = 0.05) +                                     #Lable Points (columnname3)
                geom_text(aes(x = 10, y = 800, label = "Hello there!")) +       #Random Text
                scale_x_log10() +                                               #Scaled y Variable
                scale_y_log10() +                                               #Scaled x Variable
                xlab("Populations in millions (log scale)") +                   #Lable Variable x
                ylab("Total number of murders (log scale)") +                   #Lable Variable y
                ggtitle("US Gun Murders in 2010") +                             #Title
                geom_point(aes(col=columnname4), size = 3) +                    #Grouped by color
                geom_abline(intercept = log10(r), lty = 2, color = "darkgrey")
            
            r <- murders %>%
            summarize(rate = sum(total) / sum(population) * 10^6) %>%
            pull(rate)
    8.3 #3 Variable
        8.2.1 #Discrete Data [Grouped Barchart, Stacked Barchart, Stacked 100 Barchart, Separated Grouped Barchart] 
            #Sample Dataset
            library(ggplot2)
            specie <- c(rep("sorgho" , 3) , rep("poacee" , 3) , rep("banana" , 3) , rep("triticum" , 3) )
            condition <- rep(c("normal" , "stress" , "Nitrogen") , 4)
            value <- abs(rnorm(12 , 0 , 15))
            data <- data.frame(specie,condition,value)
             
            #Grouped
            ggplot(data, aes(fill=condition, y=value, x=specie)) + 
                geom_bar(position="dodge", stat="identity")
            #Stacked
            ggplot(data, aes(fill=condition, y=value, x=specie)) + 
                geom_bar(position="stack", stat="identity")
            #Stacked 100
            ggplot(data, aes(fill=condition, y=value, x=specie)) + 
                geom_bar(position="fill", stat="identity")
            #Variation
            library(ggplot2)
            library(viridis)
            library(hrbrthemes)
            
            ggplot(data, aes(fill=condition, y=value, x=specie)) + 
                geom_bar(position="stack", stat="identity") +
                scale_fill_viridis(discrete = T) +
                ggtitle("Studying 4 species..") +
                theme_ipsum() +
                xlab("")
           #Separated Grouped Barchart
           ggplot(data, aes(fill=condition, y=value, x=condition)) + 
                geom_bar(position="dodge", stat="identity") +
                scale_fill_viridis(discrete = T, option = "E") +
                ggtitle("Studying 4 species..") +
                facet_wrap(~specie) +
                theme_ipsum() +
                theme(legend.position="none") +
                xlab("")
                
8.1 #1 Variable
        8.1.1 #Continous Data [Histogram, Density]
        