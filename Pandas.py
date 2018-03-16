c1w2: Basic Data Processing with Pandas (own file Pandas)


--DEFINITIONS--

Series Data Structure
  like a mix between list and dictionary
  Always has index column

NaN = Not a Number (None type for numbers in Numpy)


--GENERAL--
Pandas uses Numpy to store Data

iloc and loc are not methods but attributes
    methods use ()
    attributes []

vectorize queries, it is a lot faster

When appending two series, it will create a new series

In Pandas dataframe all columns always have a name

Avoid chaining data, it returns a copy of a DataFrame and not a view

Each column within a DataFrame is a Series


--CREATING SERIES--

# creating a series from lists
    labels = ['a','b','c']
    my_list = [10,20,30]
    pd.Series(data=my_list,index=labels) --> simplified as pd.Series(my_list,labels)

# creating a series from a NumPy array
    arr = np.array([10,20,30])
    pd.Series(arr,labels)

# creting a series from a dictionary, dict index becomes series index

    sports = {'Archery': 'Bhutan',
              'Golf': 'Scotland',
              'Sumo': 'Japan',
              'Taekwondo': 'South Korea'}
    s = pd.Series(sports)
    print(s)

declaring index

    s = pd.Series(['Tiger', 'Bear', 'Moose'], index=['India', 'America', 'Canada'])

# adding two series, Pandas will inner join on matching indices and add any values
# with a matching index, applyin NaN to the 'outer join' records.

Series1:
USA        1
Germany    2
USSR       3
Japan      4
dtype: int64

Series2
USA        1
Germany    2
Italy      5
Japan      4
dtype: int64

Series 1 + 2
Germany    4.0
Italy      NaN
Japan      8.0
USA        2.0
USSR       NaN
dtype: float64


adding records
    series.loc['index'] = 'value'


--QUERYING A SERIES--
iloc uses numerical key to pull record
    series.iloc[NumKey]
loc uses label key to pull record
    series.iloc[Key]



--CREATING DATAFRAME--

# create from series and then combine with the following syntax

    import pandas as pd
    purchase_1 = pd.Series({'Name': 'Chris','Item Purchased': 'Dog Food','Cost': 22.50})
    purchase_2 = pd.Series({'Name': 'Kevyn','Item Purchased': 'Kitty Litter','Cost': 2.50})
    purchase_3 = pd.Series({'Name': 'Vinod','Item Purchased': 'Bird Seed','Cost': 5.00})
    df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
    df.head()

#create from file
    pd.read_csv('csvname.csv',index_col=0,skiprows=1)
    #rename using for loop
    for col in df.columns:
    if col[:2]=='01':   df.rename(columns={col:'Gold' + col[4:]}, inplace=True)
    if col[:2]=='02':   df.rename(columns={col:'Silver' + col[4:]}, inplace=True)
    if col[:2]=='03':   df.rename(columns={col:'Bronze' + col[4:]}, inplace=True)
    if col[:1]=='№':    df.rename(columns={col:'#' + col[1:]}, inplace=True)

#replaces dataframe w/o na (null) records
    df = df.dropna()

#dropping data
    df.drop(['keyValue'],inplace=True/False,axis=0forindex(default)/1forcolumn)

#creating new column/field
    df['newField'] = df.index or df['otherField']

#hierarchical indices
    df = df.set_index([field1, field2])
    df.loc['index1','index2'] #one index
    df.loc[ [('index1','index2'), ('index1','index2')] ] #two + indices

    df = df.set_index([df.index, 'Name']) #create new hierarchical index from original index + anohter
    df.index.names = ['Location', 'Name'] #renames index
    df = df.append(pd.Series(data={'Cost': 3.00, 'Item Purchased': 'Kitty Food'}, name=('Store 2', 'Kevyn')))
    #appends a record

    #selecting a specific value from hierarchical index, work from outside in
    df.loc['G2'].loc[3]['B'] #df.loc[OuterIndex].loc[InnerIndex][Column]

    #select all inner indices regardless of outer indices
    df.xs(1,level=num) #grab all data where inner index (level) num = 1

#fills na values with something you want
    df.fillna()

#reset index
    df.reset_index(inplace=0(defualt)or1) # note original index will become column called index

#set_index


--QUERYING A DATAFRAME--

#show first 5 records
    df.head(OptionalNumber,5isDefault)

#to return a column (aka a Series) from within a DataFrame, use following syntaxself.
    dataframe['key']

#looking at one key values only
    loc['key','field']

#looking at multiple key column pairs
    loc[['List,Of,Rows'],['List,Of,Columns']]

#looking at multiple columns, submit a list of columns.
    df[['column1','column2','etc']]

# : colon reprents slices, if no slices are defined : returns all data
    df.loc[:,('field','field2')]

# shape of DataFrame
    df.shape #returns (rows,columns) of df

# returns full boolean mask
    df[df>0] #will return NaN for all values <0

# returns conditional results based on boolean mask
    df[df['column1']>0] #returns entire data frame where column1 > 0, despite other columns

# returns conditional array
    df[df['W']>0][['Y','X']]
    #return data df
    #with this conditiona applied df['W']>0]
    #returning only these columns [['Y','X']]

#Applying multiple conditions in Pandas, use & instead of and, | instead of or (Udemy)
    df[(df['W']>0) & (df['Y'] > 1)] #applies (df['W']>0) AND (df['Y'] > 1) to the boolean mask
    df[(df['W']>0) | (df['Y'] > 1)] #applies (df['W']>0) OR (df['Y'] > 1) to the boolean mask

#Grouping DataFrames
    df.groupby("Company").sum()


#WHERE method to return only values that match something
df.where( df.['field'] = condition & more df.['field'] = condition | etc)

#returns number of roews
len(df[ (df[IndexForDF]) ])

#returns conditional result based on dataframe in in second brackets
df['Name'][df['Cost']>3]

df['field'].unique() #basically distinct operator
