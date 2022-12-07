import bug_charts as bc
import file_imports as fi
import df_compare as dc
from os.path import exists

def main():
    '''main'''
    file_exists = exists('bug_list.csv')
    input_new = input('Enter file name of new file:')
    csv = input_new + '.csv'
    bug_df = fi.import_new(csv)
    prev_export = fi.load_prev_export(file_exists)
    prev_export = dc.update_prev_export(prev_export, bug_df)
    bug_delta = dc.compare_delta(bug_df, prev_export)
    dc.old_new_concat(bug_delta, prev_export)
    bc.count_by_priority(bug_df)
    bc.count_by_status(bug_df)
    bc.count_of_bugs_creation_date(bug_df)

if __name__ == "__main__":
    main()