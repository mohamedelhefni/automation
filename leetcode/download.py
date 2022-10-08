#!/usr/bin/python3

import os
import requests
import sys
from bs4 import BeautifulSoup

def go_template(description,code):
    return f"""package main




{description}



{code}


func main() {{

}}
    """






url = ""
if len(sys.argv) == 1:
    url = input("Enter Leetcode Problem URL: ")
else:
    url = sys.argv[1]


url = url[:-1] if url[-1] == '/' else url
slug = url.split("/")[-1]

headers = {
    'authority': 'leetcode.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.8',
    'origin': 'https://leetcode.com',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'x-newrelic-id': 'UAQDVFVRGwEAXVlbBAg=',
}

json_data = {
    'operationName': 'questionData',
    'variables': {
        'titleSlug': slug,
    },
    'query': 'query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n        title\n    titleSlug\n    content\n                codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n      }\n}\n',
}

response = requests.post('https://leetcode.com/graphql', headers=headers, json=json_data)
question = response.json()['data']['question']
content = BeautifulSoup(question['content'], features="html.parser")
title = question['title'].replace(" ", "")
goCode = [lang['code'] for lang in question['codeSnippets'] if lang['lang'] == 'Go'][0]
description = "// " + content.get_text().replace("\n", "\n// ")
os.mkdir(title)
with open(f"{title}/main.go", "w") as f :
    f.write(go_template(description, goCode))
    

