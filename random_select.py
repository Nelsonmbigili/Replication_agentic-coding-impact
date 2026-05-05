import pandas as pd

df = pd.read_csv('data/repos_with_details.csv')

# Filter for repositories that have at least 1 agent PR
agent_repos = df[df['num_agent_prs'] > 0]

# Randomly sample 3 repositories
sampled = agent_repos.sample(n=3) 

print(sampled[['name', 'url', 'first_agent_adopted_at']])