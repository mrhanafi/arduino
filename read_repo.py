import os
from git import Repo

COMMITS_TO_PRINT = 5

def print_commit(commit):
	print('----')
	print(str(commit.hexsha))
	print("\"{}\" byy {} ({})".format(commit.summary,
					  commit.author.name,
					  commit.author.email))
	print(str(commit.authored_datetime))
	print(str("count: {} and size: {}".format(commit.count(),
						  commit.size)))

def print_repository(repo):
	print('Repo description: {}'.format(repo.description))
	print('Repo active branch is {}'.format(repo.active_branch))
	for remote in repo.remotes:
		print('Remote named "{}" with URL "{}"'.format(remote, remote.url))
	print('Last commit for repo is {}.'.format(str(repo.head.commit.hexsha)))

def print_pull_repo(repo):
	for remote in repo.remotes:
		print('Try pull repo: {}'.format(remote.url))
		origin = repo.remotes.origin
		origin.pull()

if __name__ == "__main__":
	repo_path = os.getenv('GIT_REPO_PATH')
	#Repo object used to programmatically interact with Git repo
	repo = Repo(repo_path)
	#check that the rep loaded correctly
	if not repo.bare:
		print('Repo at {} successfully loaded.'.format(repo_path))
		print_repository(repo)
		print_pull_repo(repo)
		#create list of commits then print some of them to stdout
		commits = list(repo.iter_commits('master'))[:COMMITS_TO_PRINT]
		
		for commit in commits:
			print_commit(commit)
			pass
		else:
			print('Could not load repo at {} :('.format(repo_path))

		#print_pull_repo(repo)
