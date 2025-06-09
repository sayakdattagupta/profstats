A barebones GitHub profile README that only shows the language usage stats. Powered using Python, the GitHub REST API and GitHub Actions.

I am not using an API Key here since I am updating this once fairly conservatively (once every hour) (The API supports upto 60 calls per hour without any key).

The API call breaks downs like this:
One call for starters, and one more call for every 100 repos.
One call for each repo.
So, the limit for a user updating once each hour is 59 repos. (1 call + 59 repos = 60)

# Usage
1. Make a repo with a name exactly the same as your GitHub username.
2. Copy the source code into that. Replace ``$GITHUBUSERNAME`` in ``main.py`` with your actual username. 
3. Configure GitHub Actions workflow frequency to your liking. 60 calls per hour is the rate limit. Be wary of calling the API through the same IP adress, without a key, for other projects.
