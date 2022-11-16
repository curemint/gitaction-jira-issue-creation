# gitaction-jira-issue-creation

Terzo Jira Ticket Creation Github Action

Create a jira ticket when an action is triggered. Requiring few properties to make an API call using JIRA rest api framework.

## Getting Started

### Inputs

* JIRA_URL: Base url of your JIRA account
* JIRA_USER: JIRA user/bot email to be used for Issue creation
* JIRA_USER_TOKEN: JIRA API key for the above user
* JIRA_PROJECT: JIRA Project key
* JIRA_TICKET_SUMMARY: Summary for the created JIRA issue
* JIRA_TICKET_DESCRIPTION: Issue description
* JIRA_ISSUE_TYPE: Bug/Task


### Sample Usage

```
job:
    name: Jira Issue Creation
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Jira Issue Creation
        uses: curemint/gitaction-jira-issue-creation@master
        env:
          JIRA_URL: ${{ BASE_URL }}
          JIRA_USER: ${{ USER_MAIL }}
          JIRA_USER_TOKEN: ${{ ACCESS_TOKEN }}
          JIRA_PROJECT: ${{ $PROJECT_KEY }}
          JIRA_TICKET_SUMMARY: ${{ TITLE }}
          JIRA_TICKET_DESCRIPTION: ${{ DESCRIPTION }}
          JIRA_ISSUE_TYPE: ${{ ISSUE_TYPE }} # Bug Or Task
```

### Dependencies

* python 3.9
* requests 2.27.1
* JIRA Rest Api v3
  * For more https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/a

### References

https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions
https://docs.github.com/en/actions/creating-actions/metadata-syntax-for-github-actions

