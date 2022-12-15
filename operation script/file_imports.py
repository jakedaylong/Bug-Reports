import pandas as pd

def import_new(csv):
    '''import new csv file into bug_df dataframe based on user input gathered in main().
    dates are parsed into pandas format from csv export.'''
    bug_df = pd.read_csv(csv, index_col='Key', parse_dates=['Created', 'Updated'])
    bug_df['Created'] = bug_df['Created'].dt.date
    bug_df['Updated'] = bug_df['Updated'].dt.date
    bug_df = bug_df.sort_values(by=('Priority'), ascending=True)
    return bug_df

def load_prev_export(file_exists):
    '''loads previous export. if known previous file exists, it will use that, else it will prompt
    user to additional file name for import.'''
    if file_exists is True:
        prev_export = pd.read_csv('bug_list.csv', index_col='Key', parse_dates=['Created', 'Updated'])
        prev_export['Created'] = prev_export['Created'].dt.date
        prev_export['Updated'] = prev_export['Updated'].dt.date
    else:
        input_prev = input('Enter file name of previous file:')
        prev_csv = input_prev + '.csv'
        prev_export = pd.read_csv(prev_csv, index_col='Key', parse_dates=['Created', 'Updated'])
        prev_export['Created'] = prev_export['Created'].dt.date
        prev_export['Updated'] = prev_export['Updated'].dt.date
    return prev_export

def create_bug_df_cumsum_res(bug_df):
    bug_df_count_upd = bug_df.groupby('Updated').count()
    bug_df_count_upd['Res_Sum'] = bug_df_count_upd['Resolution']
    bug_df_cumsum_res = bug_df_count_upd.cumsum()
    return bug_df_cumsum_res

def create_bug_df_cumsum(bug_df):
    bug_df_count = bug_df.groupby('Created').count()
    bug_df_count['Adj_Sum'] = bug_df_count['Type'] - bug_df_count['Resolution']
    bug_df_cumsum = bug_df_count.cumsum()
    return bug_df_cumsum