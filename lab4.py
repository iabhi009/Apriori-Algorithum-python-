"""
Created on Mon Nov 25 11:25:24 2019
@author: iabhi
"""

import pandas as pd
glist=[]
# Program to print all combination 
# of size r in an array of size n 

# The main function that prints 
# all combinations of size r in 
# arr[] of size n. This function 
# mainly uses combinationUtil() 
def printCombination(arr, n, r,glist):	
	data = [0]*r    
	combinationUtil(arr, data, 0, n - 1, 0, r,glist)
    
    
    
    #hello
             
# arr[] ---> Input Array 
# data[] ---> Temporary array to 
#		 store current combination 
# start & end ---> Staring and Ending 
#			 indexes in arr[] 
# index ---> Current index in data[] 
# r ---> Size of a combination 
# to be printed 
def combinationUtil(arr, data, start, 
					end, index, r,glist):
    
    l=[]
	# Current combination is ready 
	# to be printed, print it 
    if (index == r): 
        for j in range(r): 
            l.append(data[j]-1)
        glist.append(l)
        return

	# replace index with all 
	# possible elements. The 
	# condition "end-i+1 >= 
	# r-index" makes sure that 
	# including one element at 
	# index will make a combination 
	# with remaining elements at 
	# remaining positions 
    i = start; 
    while(i <= end and end - i + 1 >= r - index): 
    	data[index] = arr[i]; 
    	combinationUtil(arr, data, i + 1, end, index + 1, r,glist); 
    	i += 1; 

# Driver Code 


# This code is contributed by mits 


#to check two list 
def check(org,test):
    len_org=len(org)
    len_test=len(test)
    flag=False
    for x in test:
        flag=False
        for y in org:
            #print(x,y)
            if x == y:
                flag=True
        if flag==True:
            continue
        else:
            return False
    #print("Org", len_org)
    #print("Test",len_test)
    return True



def apriori(df,i_count):
    l=[]
    cols=df.columns.values    
    #Group by 1st coloumn
    rs=df.groupby(cols[0])
    item=df[df.columns.values[1]]
    item=item.drop_duplicates()
    item_len=item.shape[0]
    print(item_len)
    itm=list(item)
    if df.shape[1] != 2:
        print("Invalid arguments passed")
        return ["Invalid"]
    print("Shape at start : ",item.shape)
    # Get the labels of rows
    glist=[]
    arr = [x for x in range(1,len(itm)+1)] 
    r = 5
    n = len(arr) 
    pattern=[]
    for x in range(1,r):
        pattern=[]
        glist=[]
        printCombination(arr, n, x,glist)
        for y in glist:
            if(len(y)<2):
                n=y[0]
                pattern.append([itm[n],0])
            else:
                l=[]
                for z in y:
                    l.append(itm[int(z)])
                l.append(0)
                pattern.append(l)
        print(x,">")
        #Contains all the permunation of x places
        #print(pattern)
        for x,y in rs:
            flag=False
            group=rs.get_group(x)
            #group=list(group)
            group=group.drop_duplicates(subset ="Item")
            for pat_itm in pattern:   
                #with count
                #print("CHECK SIZE",len(pat_itm))
                flag= check(list(group["Item"]),pat_itm[:-1])         
                #print(pat_itm)
                if flag == True:
                    pat_itm[len(pat_itm)-1]=int(pat_itm[len(pat_itm)-1])+1  
        print(pattern)
        print("Shape at last :",item.shape)
    return l
    

filename = 'hello.csv'
result= pd.read_csv(filename)
result.drop("Date",axis=1,inplace=True)
apriori(result,4)
#print(str(check([1,2,3,4],[1])))