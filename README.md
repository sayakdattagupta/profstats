A barebones GitHub profile README that only shows the language usage stats. Powered using Python, the GitHub REST API and GitHub Actions.

I am not using an API Key here since I am updating this once every 10 minutes (The API supports upto 60 calls per hour without any key).

# Usage
1. Make a repo with a name exactly the same as your GitHub username.
2. Copy the source code into that. Replace ``$GITHUBUSERNAME`` in ``main.py`` with your actual username. 
3. Configure GitHub Actions workflow frequency to your liking. 60 calls per hour is the rate limit. Be wary of calling the API through the same IP adress, without a key, for other projects.
