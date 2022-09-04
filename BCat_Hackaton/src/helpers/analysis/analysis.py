from heapq import merge
import pandas as pd
import traceback


def get_unique_pairs(posts_df,comments_df):

    tuples = []
    merge_df = []
    
    try:
        if (posts_df.empty and comments_df.empty):
            return []
        elif (posts_df.empty and not comments_df.empty):
            merge_df = comments_df[["author","subreddit"]]
        elif (not posts_df.empty and comments_df.empty):
            merge_df = posts_df[["author","subreddit"]]
        else:
            merge_df = pd.concat([posts_df[["author","subreddit"]],comments_df[["author","subreddit"]]],
                                 keys=["author","subreddit"])
                            
        merge_df = merge_df.value_counts().reset_index(name="count").sort_values(by="count",ascending=False) 

    
        for x in range(0,len(merge_df)):
            if merge_df.iloc[x]["author"] == "[deleted]" or merge_df.iloc[x]["author"] == "AutoModerator":
                continue
            tuples.append((merge_df.iloc[x]["author"],
                         1,
                         merge_df.iloc[x]["subreddit"],
                         2,
                         merge_df.iloc[x]["count"]))
    except Exception as e:
        print(e,traceback.format_exc())

    return tuples