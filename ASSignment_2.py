def answer_one(self):
    answer = self[self['Gold.2'] == max(self['Gold.2'])]
    return answer.index[0]
answer_one(df)


def answer_two(self):
    df = self[ (self['Gold'] > 0) & (self['Gold.1'] > 0) ]
    df['diff'] = df['Gold'] - df['Gold.1']
    answer = df[df['diff'] == max(df['diff'])]
    return answer.index[0]
answer_two(df)


def answer_three(self):
    df = self[ (self['Gold'] > 0) & (self['Gold.1'] > 0) ]
    df['diff'] = df['Gold'] - df['Gold.1']
    df['diff_over_total'] = df['diff']/df['Gold.2']
    answer = df[ df['diff_over_total'] == max(df['diff_over_total'] ) ]
    return answer.index[0]
answer_three(df)


def answer_four(self):
    self['Points'] = (self['Gold.2']*3) + (self['Silver.2']*2) + (self['Bronze.2']*1)
    Points = pd.Series(self['Points'].to_dict())
    return Points
answer_four(df)


def answer_five(df):
    df = df[df['SUMLEV'] == 50]
    df = df[['STNAME','SUMLEV']]
    df = df.groupby('STNAME').sum()
    answer = df[df['SUMLEV'] == max(df['SUMLEV'])]
    return answer.index[0]

answer_five(census_df)


def answer_six(df):
    df = df[['STNAME','CENSUS2010POP']]
    df = df.groupby('STNAME').sum()
    df.sort_values('CENSUS2010POP',ascending=False,inplace=True)
    df = df.head(3)
    df.reset_index(inplace=True)
    answer = list()
    for i in df['STNAME']:
        answer.append(i)
    return answer

answer_six(census_df)


def answer_seven(df):
    df = df[df['SUMLEV'] == 50]
    df.set_index(['STNAME', 'CTYNAME'],inplace=True)

    for i in df.index:
        for i in range(10,16):
            i = 'POPESTIMATE20'+str(i)
            out = df['POPESTIMATE20'+str(i)]
            print(out)

answer_seven(census_df)
