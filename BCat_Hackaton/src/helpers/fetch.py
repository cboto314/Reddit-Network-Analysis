import csv
import pandas as pd
import helpers.analysis.analysis as an

def get_nodes(api,root_node,depth,max_edges,scrape_limit,export):

    queue = [[] for x in range(depth)]
    done = []
    network = []


    queue[0].append(root_node)

    for i in range(depth):
        while not len(queue[i])==0:
            print(queue)

            node = queue[i].pop(0)

            posts_df, comments_df = scrape_content(node,api,scrape_limit,export)

            if (len(posts_df) == 0 and len(comments_df) == 0):
                continue

            unique = an.get_unique_pairs(posts_df,comments_df)
            #unique = unique[:min((len(unique)),max_edges)]

            #Find index of other nodes
            nodeIndex = 2 if node[0] == unique[0][0] else 0

            j = 0
            for tuple in unique:
                if tuple is None:
                    continue
                if (tuple not in network):
                    network.append(tuple)

                otherNode = (tuple[nodeIndex],tuple[nodeIndex+1])
                if not (i==depth-1) and not (j > min((len(unique)),max_edges)):
                    if not ((otherNode in done) or (otherNode in queue[i+1])):
                        #if not (len(queue[i])>queue_thresh):
                            queue[i+1].append(otherNode)
                j+=1


            done.append(node)

    return network

def scrape_content(node,api,scrape_limit,export):

    posts, comments = fetch_content(node,api,scrape_limit)
    

    posts_df = pd.DataFrame(posts)
    comments_df = pd.DataFrame(comments)

    if export:
        posts_df.to_csv('posts.csv')
        comments_df.to_csv('comments_df')

    return posts_df, comments_df


def fetch_content(node,api,scrape_limit):
    posts = []
    comments = []

    while True:
        try:    
            # Fetch all posts
            match node[1]:
                case 1:
                    posts = api.search_submissions(author=node[0], mem_safe=True, limit=scrape_limit)
                case 2:
                    posts = api.search_submissions(subreddit=node[0], mem_safe=True, limit=scrape_limit)
        except Exception as e:
                print(e)
                continue
        else:
                break
    while True:
        try:
            # Fetch all comments
            match node[1]:
                case 1:
                    comments = api.search_comments(author=node[0],  mem_safe=True, limit=scrape_limit)
                case 2:
                    comments = api.search_comments(subreddit=node[0],  mem_safe=True, limit=scrape_limit)
        except Exception as e:
                print(e)
                continue
        else:
                break

    return posts, comments