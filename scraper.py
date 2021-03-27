from flask import Flask, request, jsonify, redirect
import requests
from bs4 import BeautifulSoup as bs

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/') 
def welcome():
    return "<h1>Welcome to Python Web Service</h1><h3><b>Done By :</b><br>Maalolan K<br><ul><li>To get link of profile image of a user with username <user>, type https://maalolankannan1.github.io/<user></li>"

@app.route('/<git_user>')
def get_image(git_user):
    url = 'https://github.com/'+git_user
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    profile_image = soup.find('img', {'alt' : 'Avatar'})['src']
    print("Link for the Profile Image : " + profile_image)
    return "<a href = {profile_image}>Click here to open</a>"

# #git_user = input('Enter Github username: ')
# url = 'https://github.com/'+git_user+'?tab=repositories'
# r = requests.get(url)
# soup = bs(r.content, 'html.parser')
# profile_image = soup.find('img', {'alt' : 'Avatar'})['src']
# print("Link for the Profile Image : " + profile_image)
# all_repos = soup.findAll('li', {'itemprop' : 'owns'})
# repo_names = []
# for repo in all_repos:
#     repo_names.append(repo.find('a',{'itemprop' : 'name codeRepository'}).get_text())
# ## repo_names contains list of all repos
# print(" The Repositories of " + git_user + " :\n")
# for repo in repo_names:
#     print(repo)

if(__name__ == "__main__"):
    app.run()