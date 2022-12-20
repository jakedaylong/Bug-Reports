import bug_charts as bc
import file_imports as fi
import df_compare as dc
from os.path import exists

def main():
    '''main'''
    file_exists = exists('bug_list.csv')
    csv_unres = input('Enter file name of unresolved bug file:')
    csv_res = input('Enter file name of resolved bug file:')
    bug_unresolved = fi.import_new(csv_unres)
    bug_resolved = fi.import_new(csv_res)
    bug_df = dc.unresolved_resolved_concat(bug_unresolved, bug_resolved)
    prev_export = fi.load_prev_export(file_exists)
    prev_export = dc.update_prev_export(prev_export, bug_df)
    bug_delta = dc.compare_delta(bug_df, prev_export)
    bug_df_cumsum_res = fi.create_bug_df_cumsum_res(bug_df)
    bug_df_cumsum = fi.create_bug_df_cumsum(bug_df)
    dc.old_new_concat(bug_delta, prev_export)
    bc.count_by_priority(bug_df)
    bc.count_by_status(bug_df)
    bc.count_of_bugs_creation_date(bug_df)
    bc.cumsum_total_res(bug_df_cumsum, bug_df_cumsum_res)

if __name__ == "__main__":
    main()