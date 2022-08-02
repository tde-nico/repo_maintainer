import os
import requests
import json
import git


USERNAME = 'tde-nico'
FOLDER = '.' # '.' -> local folder


def get_repos(username):
	names = []
	page_number = 1
	while page_number <= 100:
		responce = requests.get(f'https://api.github.com/users/{username}/repos?page={page_number}')
		page_repos = json.loads(responce.text)
		if not page_repos:
			break
		names += [repo['name'] for repo in page_repos]
		page_number += 1
	return names


def maintain(username, name):
	if os.path.exists(name):
		print(f'[+] pulling {name}')
		repo = git.cmd.Git(name)
		repo.pull()
	else:
		print(f'[+] cloning {name}')
		git.Repo.clone_from(f'https://github.com/{username}/{name}', name)


def main():
	if not os.path.exists(FOLDER):
		os.mkdir(FOLDER)
	os.chdir(FOLDER)
	names = get_repos(USERNAME)
	for name in names:
		maintain(USERNAME, name)


if __name__ == '__main__':
	main()
