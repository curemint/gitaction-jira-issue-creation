# This code sample uses the 'requests' library:
# http://docs.python-requests.org
# Used JIRA REST API Version 3
# Ref: https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/
import os
import re
import requests
from requests.auth import HTTPBasicAuth
import json


class Inputs:
    JIRA_BASE_URL = os.getenv("JIRA_URL")
    JIRA_USER = os.getenv("JIRA_USER")
    JIRA_USER_TOKEN = os.getenv("JIRA_USER_TOKEN")
    JIRA_PROJECT = os.getenv("JIRA_PROJECT")
    JIRA_TICKET_SUMMARY = os.getenv("JIRA_TICKET_SUMMARY")
    JIRA_TICKET_DESCRIPTION = os.getenv("JIRA_TICKET_DESCRIPTION")
    JIRA_ISSUE_TYPE = os.getenv("JIRA_ISSUE_TYPE")
    JIRA_ISSUE_LINK = re.findall(r'\[(.*?)\]', JIRA_TICKET_SUMMARY)[0]

createIssueUrl = Inputs.JIRA_BASE_URL + "/rest/api/3/issue"
issueLinkUrl = Inputs.JIRA_BASE_URL + "/rest/api/3/issueLink"

auth = HTTPBasicAuth(Inputs.JIRA_USER, Inputs.JIRA_USER_TOKEN)
headers = {"Accept": "application/json", "Content-Type": "application/json"}


def createIssue():
    createIssuePayload = json.dumps(
        {
            "fields": {
                "summary": Inputs.JIRA_TICKET_SUMMARY,
                "issuetype": {"name": Inputs.JIRA_ISSUE_TYPE},
                "project": {"key": Inputs.JIRA_PROJECT},
                "description": {
                    "type": "doc",
                    "version": 1,
                    "content": [
                        {"type": "paragraph", "content": [{"text": Inputs.JIRA_TICKET_DESCRIPTION, "type": "text"}]}
                    ],
                },
            }
        }
    )

    createIssueResponse = requests.request("POST", createIssueUrl, data=createIssuePayload, headers=headers, auth=auth)
    return createIssueResponse


def linkIssue(issueKey):
    linkIssuePayload = json.dumps(
        {
            "outwardIssue": {"key": issueKey},
            "inwardIssue": {"key": Inputs.JIRA_ISSUE_LINK},
            "type": {"name": "Relates"},
        }
    )
    linkIssueReponse = requests.request("POST", issueLinkUrl, data=linkIssuePayload, headers=headers, auth=auth)
    if linkIssueReponse.ok:
        print(
            "Outward Issue : "
            + issueKey
            + " and Inward Issue : "
            + Inputs.JIRA_ISSUE_LINK
            + " Issue Linked Successfully!"
        )
    else:
        print("Linking Issues Failed!!")


if __name__ == "__main__":
    createIssueResponse = createIssue()
    if createIssueResponse.ok:
        createdIssueKey = json.loads(createIssueResponse.text)["key"]
        print("Key : " + createdIssueKey + " Issue Created Successfully!")
        linkIssue(createdIssueKey)
    else:
        print("Issue not created!!")
