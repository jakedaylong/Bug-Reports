import matplotlib.pyplot as plt
import seaborn as sns
import mpld3

def count_of_bugs_creation_date(bug_df):
    '''Creates histplot for count of bugs by creations date from bug_df dataframe
    and colored by bug priority. (includes resolved bugs)'''
    fig, ax = plt.subplots(figsize=(12,8))
    palette = {'Blocker':'tab:red', 'Major':'tab:orange', 'Minor':'tab:green', 'Trivial':'tab:blue'}
    sns.set_context('notebook')
    sns.histplot(data=bug_df, x='Created', hue='Priority', multiple='stack', palette=palette)
    plt.savefig(fname='Count_of_Bugs_Creation_Date')
    
    html_str = mpld3.fig_to_html(fig)
    html_file= open("Count_by_Priority.html","w")
    html_file.write(html_str)
    html_file.close()

def count_by_priority(bug_df):
    '''count of total bugs by priority. (includes resolved bugs)'''
    bug_df = bug_df.sort_values(by='Status', ascending=True)
    fig, ax = plt.subplots(figsize=(12,8))
    palette = {'Customer Action':'tab:red','In Progress':'tab:blue', 'Open':'tab:orange', 'Resolved':'tab:green', 'in Discussion':'tab:grey'}
    sns.set_context('notebook')
    sns.histplot(data=bug_df, x='Priority', hue='Status', multiple='stack', palette=palette)
    plt.savefig(fname='Count_by_Priority')

    html_str = mpld3.fig_to_html(fig)
    html_file= open("Count_by_Priority.html","w")
    html_file.write(html_str)
    html_file.close()

def count_by_status(bug_df):
    '''count of bugs by current status. colored by priotity. (includes resolved bugs)'''
    bug_df = bug_df.sort_values(by='Priority', ascending=True)
    fig, ax = plt.subplots(figsize=(12,8))
    palette = {'Blocker':'tab:red', 'Major':'tab:orange', 'Minor':'tab:green', 'Trivial':'tab:blue'}
    sns.set_context('notebook')
    sns.histplot(data=bug_df, x='Status', hue='Priority', multiple='stack', palette=palette)
    plt.savefig(fname='Count_by_Status')
    
    html_str = mpld3.fig_to_html(fig)
    html_file= open("Count_by_Status.html","w")
    html_file.write(html_str)
    html_file.close()

def cumsum_total_res(bug_df_cumsum, bug_df_cumsum_res):
    fig, ax = plt.subplots(figsize=(12,8))
    plt.xticks(rotation=45)
    sns.lineplot(data=bug_df_cumsum, x='Created', y='Type', marker='o', legend=True, label='Cumulative Sum')
    sns.lineplot(data=bug_df_cumsum_res, x='Updated', y='Res_Sum', marker='o', legend=True, label='Resolution Cumulative Sum')
    plt.savefig(fname='Cumsum_Total_vs_Resolved')

    html_str = mpld3.fig_to_html(fig)
    html_file= open("Sum_Total_vs_Resolved.html","w")
    html_file.write(html_str)
    html_file.close()

def count_of_bugs_resolved(bug_df):
    '''Creates histplot for count of bugs by creations date from bug_df dataframe
    and colored by bug status. (includes resolved bugs)'''
    fig, ax = plt.subplots(figsize=(12,8))
    palette = {'Customer Action':'tab:red', 'In Progress':'tab:orange', 'Resolved':'tab:green', 'in Discussion':'tab:blue'}
    sns.set_context('notebook')
    sns.histplot(data=bug_df, x='Created', hue='Status', multiple='stack')
    plt.savefig(fname='Count_of_Bugs_Resolved')