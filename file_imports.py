#pylint: disable=line-too-long
'''Scripting for file imports'''
import pandas as pd

def multi_file_unres(csv_unres_count):
    '''created to support multiple file upload'''
    count = 1
    bug_unresolved = pd.DataFrame()
    while count <= csv_unres_count:
        csv_unres = input('Enter file name of unresolved bug file ' + str(count) + ':')
        unres_df = import_new(csv_unres)
        bug_unresolved = pd.concat([bug_unresolved, unres_df])
        count += 1
    return bug_unresolved

def multi_file_res(csv_res_count):
    '''created to support multiple file upload'''
    count = 1
    bug_resolved = pd.DataFrame()
    while count <= csv_res_count:
        csv_res = input('Enter file name of resolved bug file ' + str(count) + ':')
        res_df = import_new(csv_res)
        bug_resolved = pd.concat([bug_resolved, res_df])
        count += 1
    return bug_resolved

def import_new(csv):
    '''import new csv file into csv_import dataframe based on user input gathered in main().
    dates are parsed into pandas format from csv export.'''
    csv_import = pd.read_csv(csv, index_col='Key', parse_dates=['Created', 'Updated'], encoding="cp1252")
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

def counts_greater_than_one_unresolved(csv_unres_count):
    '''added functionality for the existence of more than one file to upload at a time'''
    if csv_unres_count > 1:
        bug_unresolved = multi_file_unres(csv_unres_count)
    else:
        csv_unres = input('Enter file name of unresolved bug file:')
        bug_unresolved = import_new(csv_unres)
    return bug_unresolved

def counts_greater_than_one_resolved(csv_res_count):
    '''added functionality for the existence of more than one file to upload at a time'''
    if csv_res_count > 1:
        bug_resolved = multi_file_res(csv_res_count)
    else:
        csv_res = input('Enter file name of resolved bug file:')
        bug_resolved = import_new(csv_res)
    return bug_resolved
