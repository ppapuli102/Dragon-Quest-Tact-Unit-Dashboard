import pandas as pd

## Viewing Options for pandas in terminal
pd.set_option('max_columns', None)
pd.set_option('max_colwidth', 100)
pd.options.display.width = None

def clean_database(dqt):

    def splitSkillsInfo(s):
        return s.split('\n')

    def splitSkillInfoComma(s):
        try:
            return s.split(',')
        except AttributeError:
            return s

    def splitDescriptionColon(s):
        try:
            return s.split(': ')
        except AttributeError:
            return s

    def firstInArray(a):
        try:
            return a[0]
        except TypeError:
            return a

    def secondInArray(a):
        try:
            return a[1]
        except TypeError:
            return a
        except IndexError:
            return a

    def thirdInArray(a):
        try:
            return a[2]
        except TypeError:
            return a
        except IndexError:
            return a

    def changeNonetoTypeless(s):
        if s == 'None':
            s='Typeless'
        return s

    def stripString(s):
        try:
            return s.strip()
        except AttributeError:
            return s

    dqt = dqt.fillna('')

    ## Split the Skill Info into an Array with its components
    dqt['Skill 1 - Info'] = dqt['Skill 1 - Info'].apply(splitSkillsInfo)
    ## Split the first skill in the array into its two components for two new columns
    dqt['Skill 1 - Infos'] = dqt['Skill 1 - Info'].apply(firstInArray)
    dqt['Skill 1 - Infos'] = dqt['Skill 1 - Infos'].apply(splitSkillInfoComma)
    dqt['Skill 1 - Damage Type'] = dqt['Skill 1 - Infos'].apply(firstInArray)
    dqt['Skill 1 - Damage Type'] = dqt['Skill 1 - Damage Type'].apply(stripString)
    dqt['Skill 1 - Damage Element'] = dqt['Skill 1 - Infos'].apply(secondInArray)
    dqt['Skill 1 - Damage Element'] = dqt['Skill 1 - Damage Element'].apply(stripString)
    dqt['Skill 1 - Damage Element'] = dqt['Skill 1 - Damage Element'].apply(changeNonetoTypeless)
    ## Create the columns for the remaining components of skill info
    dqt['Skill 1 - Type/Range'] = dqt['Skill 1 - Info'].apply(secondInArray)
    dqt['Skill 1 - Cost'] = dqt['Skill 1 - Info'].apply(thirdInArray)
    ## Split the Skill Description into two columns
    dqt['Skill 1 - Description Split'] = dqt['Skill 1 (+0) Description'].apply(splitDescriptionColon)
    dqt['Skill 1 - Name'] = dqt['Skill 1 - Description Split'].apply(firstInArray)
    dqt['Skill 1 - Description'] = dqt['Skill 1 - Description Split'].apply(secondInArray)

    ### Repeat the same steps for skills 2 and 3
    ## Split the skill info into its components
    dqt['Skill 2 - Info'] = dqt['Skill 2 - Info'].apply(splitSkillsInfo)
    ## Split the second skill in the array into its two components for two new columns
    dqt['Skill 2 - Infos'] = dqt['Skill 2 - Info'].apply(firstInArray)
    dqt['Skill 2 - Infos'] = dqt['Skill 2 - Infos'].apply(splitSkillInfoComma)
    dqt['Skill 2 - Damage Type'] = dqt['Skill 2 - Infos'].apply(firstInArray)
    dqt['Skill 2 - Damage Type'] = dqt['Skill 2 - Damage Type'].apply(stripString)
    dqt['Skill 2 - Damage Element'] = dqt['Skill 2 - Infos'].apply(secondInArray)
    dqt['Skill 2 - Damage Element'] = dqt['Skill 2 - Damage Element'].apply(stripString)
    dqt['Skill 2 - Damage Element'] = dqt['Skill 2 - Damage Element'].apply(changeNonetoTypeless)
    ## Create the columns for the remaining components of skill info
    dqt['Skill 2 - Type/Range'] = dqt['Skill 2 - Info'].apply(secondInArray)
    dqt['Skill 2 - Cost'] = dqt['Skill 2 - Info'].apply(thirdInArray)
    ## Split the Skill Description into two columns
    dqt['Skill 2 - Description Split'] = dqt['Skill 2 (+0) Description'].apply(splitDescriptionColon)
    dqt['Skill 2 - Name'] = dqt['Skill 2 - Description Split'].apply(firstInArray)
    dqt['Skill 2 - Description'] = dqt['Skill 2 - Description Split'].apply(secondInArray)

    ### Skill 3 Cleaning
    ## Split the skill info into its components
    dqt['Skill 3 - Info'] = dqt['Skill 3 - Info'].apply(splitSkillsInfo)
    ## Split the second skill in the array into its two components for two new columns
    dqt['Skill 3 - Infos'] = dqt['Skill 3 - Info'].apply(firstInArray)
    dqt['Skill 3 - Infos'] = dqt['Skill 3 - Infos'].apply(splitSkillInfoComma)
    dqt['Skill 3 - Damage Type'] = dqt['Skill 3 - Infos'].apply(firstInArray)
    dqt['Skill 3 - Damage Type'] = dqt['Skill 3 - Damage Type'].apply(stripString)
    dqt['Skill 3 - Damage Element'] = dqt['Skill 3 - Infos'].apply(secondInArray)
    dqt['Skill 3 - Damage Element'] = dqt['Skill 3 - Damage Element'].apply(stripString)
    dqt['Skill 3 - Damage Element'] = dqt['Skill 3 - Damage Element'].apply(changeNonetoTypeless)
    ## Create the columns for the remaining components of skill info
    dqt['Skill 3 - Range'] = dqt['Skill 3 - Info'].apply(secondInArray)
    dqt['Skill 3 - Cost'] = dqt['Skill 3 - Info'].apply(thirdInArray)
    ## Split the Skill Description into two columns
    dqt['Skill 3 - Description Split'] = dqt['Skill 3 (+0) Description'].apply(splitDescriptionColon)
    #print(dqt['Skill 3 - Description Split'])
    dqt['Skill 3 - Name'] = dqt['Skill 3 - Description Split'].apply(firstInArray)
    dqt['Skill 3 - Description'] = dqt['Skill 3 - Description Split'].apply(secondInArray)

    dqt = dqt.drop(
        columns=[
            'Skill 1 - Info',
            'Skill 1 - Infos',
            'Skill 1 (+0) Description',
            'Skill 1 - Description Split',
            'Skill 2 - Info',
            'Skill 2 - Infos',
            'Skill 2 - Description Split',
            'Skill 2 (+0) Description',
            'Skill 3 - Info',
            'Skill 3 (+0) Description',
            'Skill 3 - Infos',
            'Skill 3 - Description Split',
        ]
    )
    print('dqt columns', dqt.columns)

    return dqt

#dqt.to_csv("C:\\Users\\Peter\\Desktop\\DQT_dashboard\\unit_database_cleaned_new.csv")


## Multiple Filters on a column
#print(dqt[(dqt['Crack'] == 'Res') & (dqt['Family'] == 'Nature')])

## Group by done correctly
#print(dqt[dqt['Rarity'] == 'S'].groupby('Role').agg("mean").round(2) )

'''    dqt.columns = [
        'Name', 'Picture', 'Rank', 'Family', 'Role',
        '', '', '', '', '', '', '',
        'Max HP', 'Max MP', 'Max ATK', 'Max DEF', 'Max AGL', 'Max WIS', 'Move', '',
        'Frizz', 'Sizz', 'Crack', 'Woosh', 'Bang', 'Zap', 'Zam', '',
        'Sleep', 'Poison', 'Physical Lock', 'Spell Lock', 'Martial Lock', 'Breath_lock', 'Hobble', 'Stun', 'Blind', 'Curse', 'Paralysis', 'Confusion', 'Charm', '', 'Leader Skill', 'Coup de Grace - Info',
        'Coup de Grace Description', '1st Awakening Passive', 'Additional Passive', 'Picture Link',
        'Skill 1 - Damage Type', 'Skill 1 - Damage Element', 'Skill 1 - Type/Range', 'Skill 1 - Cost', 'Skill 1 - Name', 'Skill 1 - Description',
        'Skill 2 - Damage Type', 'Skill 2 - Damage Element', 'Skill 2 - Type/Range', 'Skill 2 - Cost', 'Skill 2 - Name', 'Skill 2 - Description',
        'Skill 3 - Damage Type', 'Skill 3 - Damage Element', 'Skill 3 - Range', 'Skill 3 - Cost', 'Skill 3 - Name', 'Skill 3 - Description',
    ]'''
