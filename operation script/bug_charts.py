import matplotlib.pyplot as plt
import seaborn as sns

def count_of_bugs_creation_date(bug_df):
    '''Creates histplot for count of bugs by creations date from bug_df dataframe
    and colored by bug priority. (includes resolved bugs)'''
    fig, ax = plt.subplots(figsize=(12,8))
    palette = {'Blocker':'tab:red', 'Major':'tab:orange', 'Minor':'tab:green', 'Trivial':'tab:blue'}
    sns.set_context('notebook')
    sns.histplot(data=bug_df, x='Created', hue='Priority', multiple='stack', palette=palette)
    plt.savefig(fname='count_of_bugs_creation_date')

def count_by_priority(bug_df):
    '''count of total bugs by priority. (includes resolved bugs)'''
    bug_df = bug_df.sort_values(by='Status', ascending=True)
    fig, ax = plt.subplots(figsize=(12,8))
    palette = {'Customer Action':'tab:red','In Progress':'tab:blue', 'Open':'tab:orange', 'Resolved':'tab:green', 'in Discussion':'tab:grey'}
    sns.set_context('notebook')
    sns.histplot(data=bug_df, x='Priority', hue='Status', multiple='stack', palette=palette)
    plt.savefig(fname='Count_By_Priority')

def count_by_status(bug_df):
    '''count of bugs by current status. colored by priotity. (includes resolved bugs)'''
    bug_df = bug_df.sort_values(by='Priority', ascending=True)
    fig, ax = plt.subplots(figsize=(12,8))
    palette = {'Blocker':'tab:red', 'Major':'tab:orange', 'Minor':'tab:green', 'Trivial':'tab:blue'}
    sns.set_context('notebook')
    sns.histplot(data=bug_df, x='Status', hue='Priority', multiple='stack', palette=palette)
    plt.savefig(fname='Count_By_Status')