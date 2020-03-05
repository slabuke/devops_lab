#!/usr/bin/env python

import argparse
import requests
import getpass

parser = argparse.ArgumentParser()
parser.add_argument("-owner", nargs=1, help="write repo owner", required=True)
parser.add_argument("-repo", nargs=1, help="write name of repo", required=True)
parser.add_argument("-number", nargs=1, help="write number of pullrequest", required=True)
parser.add_argument("-status", action="store_true", help="Pull request status")
parser.add_argument("-created", action="store_true", help="Date of creating")
parser.add_argument("-commits", action="store_true", help="Count of commits")
parser.add_argument("-comments", action="store_true", help="Number of comments")
parser.add_argument("-user", action="store_true", help="User who open")
parser.add_argument('-v', action='version', version='version 1.0')


args = parser.parse_args()

user = input("User: \n")
print("And password: ")
try:
    password = getpass.getpass()
except Exception as err:
    print("You don't entered password", err)

req = requests.get(
    'https://api.github.com/repos/' + args.owner[0] + '/' + args.repo[0] + '/pulls/' + args.number[
        0] + ".json", auth=(user, password))

r = req.json()
data = r['title']
if args.created:
    data += " Created: " + r['created_at']

if args.status:
    data += " Request_status: " + r['labels'][0]['name']

if args.user:
    data += " Opened_by: " + r['head']['repo']['owner']['login'] + " "

if args.commits:
    data += " Count_of_commits: " + str(r['commits'])

if args.comments:
    data += " Number_of_comments: " + str(r['comments'])

print(data)
