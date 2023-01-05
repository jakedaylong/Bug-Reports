#pylint: disable=line-too-long, unspecified-encoding
'''Charting script'''
import os
import matplotlib.pyplot as plt
import seaborn as sns
import mpld3

def get_dir():
    '''retreiving directories for file saving'''
    script_dir = os.path.dirname(__file__)
    png_dir = os.path.join(script_dir, 'Charts_PNG/')
    html_dir = os.path.join(script_dir, 'Charts_HTML/')
    bug_dir = os.path.join(script_dir, 'Bug_Lists/')
    return png_dir, html_dir, bug_dir

def count_of_bugs_creation_date(bug_df, png_dir, html_dir):
    '''Creates histplot for count of bugs by creations date from bug_df dataframe
    and colored by bug priority. (includes resolved bugs)'''
    fig = plt.subplots(figsize=(12,8))
    palette = {'Blocker':'tab:red', 'Major':'tab:orange', 'Minor':'tab:green', 'Trivial':'tab:blue'}
    sns.set_context('notebook')
    sns.histplot(data=bug_df, x='Created', hue='Priority', multiple='stack', palette=palette)
    plt.savefig(png_dir + 'Count_of_Bugs_Creation_Date.png')
    #html chart generation
    html_str = mpld3.fig_to_html(fig)
    html_file = open(html_dir + "Count_by_Priority.html","w")
    html_file.write(html_str)
    html_file.close()

def count_by_priority(bug_df, png_dir, html_dir):
    '''count of total bugs by priority. (includes resolved bugs)'''
    bug_df = bug_df.sort_values(by='Status', ascending=True)
    fig = plt.subplots(figsize=(12,8))
    palette = {'Customer Action':'tab:red','In Progress':'tab:blue', 'Open':'tab:orange', 'Resolved':'tab:green', 'in Discussion':'tab:grey'}
    sns.set_context('notebook')
    sns.histplot(data=bug_df, x='Priority', hue='Status', multiple='stack', palette=palette)
    plt.savefig(png_dir + 'Count_by_Priority.png')
    #html chart generation
    html_str = mpld3.fig_to_html(fig)
    html_file = open(html_dir + "Count_by_Priority.html","w")
    html_file.write(html_str)
    html_file.close()

def count_by_status(bug_df, png_dir, html_dir):
    '''count of bugs by current status. colored by priotity. (includes resolved bugs)'''
    bug_df = bug_df.sort_values(by='Priority', ascending=True)
    fig = plt.subplots(figsize=(12,8))
    palette = {'Blocker':'tab:red', 'Major':'tab:orange', 'Minor':'tab:green', 'Trivial':'tab:blue'}
    sns.set_context('notebook')
    sns.histplot(data=bug_df, x='Status', hue='Priority', multiple='stack', palette=palette)
    plt.savefig(png_dir + 'Count_by_Status.png')
    #html chart generation
    html_str = mpld3.fig_to_html(fig)
    html_file = open(html_dir + "Count_by_Status.html","w")
    html_file.write(html_str)
    html_file.close()

def cumsum_total_res(bug_df_cumsum, bug_df_cumsum_res, png_dir, html_dir):
    '''cumsum chart for active vs resolved bugs'''
    fig = plt.subplots(figsize=(12,8))
    plt.xticks(rotation=45)
    sns.lineplot(data=bug_df_cumsum, x='Created', y='Type', marker='o', legend=True, label='Cumulative Sum')
    sns.lineplot(data=bug_df_cumsum_res, x='Updated', y='Res_Sum', marker='o', legend=True, label='Resolution Cumulative Sum')
    plt.savefig(png_dir + 'Cumsum_Total_vs_Resolved.png')
    #html chart generation
    html_str = mpld3.fig_to_html(fig)
    html_file = open(html_dir + "Sum_Total_vs_Resolved.html","w")
    html_file.write(html_str)
    html_file.close()

def count_of_bugs_resolved(bug_df, png_dir, html_dir):
    '''Creates histplot for count of bugs by creations date from bug_df dataframe
    and colored by bug status. (includes resolved bugs)'''
    fig = plt.subplots(figsize=(12,8))
    #palette = {'Customer Action':'tab:red', 'In Progress':'tab:orange', 'Resolved':'tab:green', 'in Discussion':'tab:blue'}
    sns.set_context('notebook')
    sns.histplot(data=bug_df, x='Created', hue='Status', multiple='stack')
    plt.savefig(png_dir + 'Count_of_Bugs_Resolved.png')
    #html chart generation
    html_str = mpld3.fig_to_html(fig)
    html_file = open(html_dir + "Count_of_Bugs_Resolved.html","w")
    html_file.write(html_str)
    html_file.close()
    