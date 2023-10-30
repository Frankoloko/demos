import jira.client  # https://jira.readthedocs.io/examples.html#issues
 
try:
    from functools import lru_cache
except ImportError:
    from backports.functools_lru_cache import lru_cache
 
@lru_cache()  # Not sure what this does but you need it
def get_jira_connection(server="???", username="???", password="???"):
    server = "http://{0}".format(server)
    options = {"server": server}
    authentication = (username, password)
 
    connection = jira.client.JIRA(options=options, basic_auth=authentication)
 
    return connection
connection = get_jira_connection()
 
# Update a ticket(issue)
connection.issue("TICKET-1111").update({"description": "something"})
 
# Read the description
description = connection.issue("TICKET-1111").fields.description
 
# Search for tickets(issues)
jql_request = 'summary ~ "Add the repo to PR" AND description ~ "otherwise you can update"'
issues = connection.search_issues(jql_request)
print(issues[0].key)  # TICKET-1111
 
# Add a comment
issue = connection.issue("TICKET-1111")
connection.add_comment(issue, "Comment text")