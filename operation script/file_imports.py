'''Scripting for file imports'''
import pandas as pd

def import_new(csv):
    '''import new csv file into csv_import dataframe based on user input gathered in main().
    dates are parsed into pandas format from csv export.'''
    csv_import = pd.read_csv(csv, index_col='Key', parse_dates=['Created', 'Updated'])
    csv_import['Created'] = csv_import['Created'].dt.date
    csv_import['Updated'] = csv_import['Updated'].dt.date
    csv_import = csv_import.sort_values(by=('Priority'), ascending=True)
    return csv_import

def load_prev_export(file_exists, bug_dir):
    '''loads previous export. if known previous file exists, it will use that, else it will prompt
    user to additional file name for import.'''
    if file_exists is True:
        prev_export = pd.read_csv(bug_dir + 'bug_list.csv', index_col='Key', parse_dates=['Created', 'Updated'])
        prev_export['Created'] = prev_export['Created'].dt.date
        prev_export['Updated'] = prev_export['Updated'].dt.date
    else:
        prev_csv = input('Enter file name of previous file:')
        prev_export = pd.read_csv(prev_csv, index_col='Key', parse_dates=['Created', 'Updated'])
        prev_export['Created'] = prev_export['Created'].dt.date
        prev_export['Updated'] = prev_export['Updated'].dt.date
    return prev_export

def create_bug_df_cumsum_res(bug_df):
    '''creating dataframe bug_df_cumsum_res'''
    bug_df_count_upd = bug_df.groupby('Updated').count()
    bug_df_count_upd['Res_Sum'] = bug_df_count_upd['Resolution']
    bug_df_cumsum_res = bug_df_count_upd.cumsum()
    return bug_df_cumsum_res

def create_bug_df_cumsum(bug_df):
    '''creating dataframe bug_df_cumsum'''
    bug_df_count = bug_df.groupby('Created').count()
    bug_df_count['Adj_Sum'] = bug_df_count['Type'] - bug_df_count['Resolution']
    bug_df_cumsum = bug_df_count.cumsum()
    return bug_df_cumsum
