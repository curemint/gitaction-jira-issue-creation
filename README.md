# Project Title

Terzo Jira Ticket Creation Github Action

## Description

To create a jira ticket when the action triggered. Requiring few properties to make a api call with JIRA rest api framework.

## Getting Started

### Dependencies

* python 3.9
* requests 2.27.1
* JIRA Rest Api v3
  * For more https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/a

### How to use

```
job:
    name: Jira Issue Creation
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Jira Issue Creation
        uses: curemint/gitaction-jira-issue-creation@v1
        env:
          JIRA_URL: ${{ BASE_URL }}
          JIRA_USER: ${{ USER_MAIL }}
          JIRA_USER_TOKEN: ${{ ACCESS_TOKEN }}
          JIRA_PROJECT: ${{ $PROJECT_KEY }}
          JIRA_TICKET_SUMMARY: ${{ TITLE }}
          JIRA_TICKET_DESCRIPTION: ${{ DESCRIPTION }}
          JIRA_ISSUE_TYPE: ${{ ISSUE_TYPE }} # Bug Or Task
          
```
### References

https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions
https://docs.github.com/en/actions/creating-actions/metadata-syntax-for-github-actions

