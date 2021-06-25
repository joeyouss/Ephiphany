import praw

reddit = praw.Reddit(
    client_id="3CPB0JETqwQAOA",
    client_secret="t8CrdJ0dmri7MK9IJnaLuvb_tEuI-g",
    user_agent="MyPersonalBot",
)
for submission in reddit.subreddit("funny").hot(limit=10):
    print(submission.title)