import pandas as pd

def compare_delta(bug_df, prev_export):
    '''compares new import (bug_df) to previous file (prev_export) and returns the delta'''
    bug_delta = bug_df.loc[bug_df.index.difference(prev_export.index)]
    return bug_delta

def update_prev_export(prev_export, bug_df):
    '''updates row data'''
    prev_export.update(bug_df)
    return prev_export

def old_new_concat(bug_delta, prev_export):
    '''concats both the bug_df and prev_export dataframes into new bug list for export.'''
    concat_bug_df = pd.concat([prev_export, bug_delta])
    concat_bug_df.to_csv('bug_list.csv')

def unresolved_resolved_concat(bug_unresolved, bug_resolved):
    '''Concats both the resolved and unresolved lists into a single df for processing'''
    bug_df = pd.concat([bug_unresolved, bug_resolved])
    return bug_df