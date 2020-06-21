import praw

subreddit_name = "RobinhoodPennyStocks"

my_client_id = '' #removed for privacy, tutorial that explains what these are: https://towardsdatascience.com/scraping-reddit-data-1c0af3040768
my_client_secret = '' #as above
my_user_agent = '' #as above

reddit = praw.Reddit(client_id=my_client_id, client_secret=my_client_secret, user_agent=my_user_agent) #create the praw object

subreddit = reddit.subreddit(subreddit_name) #specify the subreddit of interest, for us r/RobinhoodPennyStocks
comments = subreddit.comments(limit = 50) #limit by 50 so you don't get slapped by the rate limit

for comment in comments: #print the body for every comment you just retrieved, can look at the documentation here: https://praw.readthedocs.io/en/latest/code_overview/models/subreddit.html#praw.models.Subreddit.comments
    print(comment.body)