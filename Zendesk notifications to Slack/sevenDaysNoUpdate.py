import requests
import slack
import zendeskUserMatchToSlack as zUM

# SET THE SLACK ENVIRONMENT VARIABLE
slackDev = 'xoxb-'  # place your DEV slackbot token here
slackProd = 'xoxb-'  # place your PROD slackbot token here
# SET THE SLACK ENVIRONMENT WITH TOKEN
client = slack.WebClient(token=slackDev)

# ENVIRONMENT VARIABLES FOR ZENDESK
zenDev = 'https://your_subdomain.zendesk.com/api/v2/groups.json'  # place with your SANDBOX/TEST endpoint
zenProd = 'https://your_subdomain.zendesk.com/api/v2/groups.json'  # place with your PRODUCTION endpoint

# CONTACT ZENDESK, AUTHORISE YOUR REQUEST AND STORE THE RESPONSE
response = requests.get(zenDev, auth=('email/token', 'token'))
# for more information on authentication using the api, please see here:
# https://support.zendesk.com/hc/en-us/articles/115000510267-How-can-I-authenticate-API-requests-

# DECODE THE RESPONSE INTO A DICTIONARY
data = response.json()
# print(data) ###sanity check response

# ITERATE THROUGH THE DICTIONARY
for item in data['tickets']:
    # print(zUM.slackUserLookup(item['assignee_id']))
    zenAssignee = item['assignee_id']  # find the assignee ID for each iteration
    # print(zenAssignee) ###sanity check response
    target = zUM.slackUserLookup(
        zenAssignee)  # lookup the zendeskUID using ZendeskUserMatch.py and return slackUID and store as target
    # print(target) ###sanity check response
    zenSubject = item['subject']  # store the ticket subbject
    # print(zenSubject) ###sanity check response
    zenID = str(item['id'])  # store the ticket ID
    # print(zenID) ###sanity check response

    # construct the user zendesk URL and store
    zenURL = 'https://your_subdomain.zendesk.com/agent/tickets/' + zenID
    # print(zenURL) ###sanity check response

    # CONSTRUCT AND SEND THE MESSAGE TO SLACK
    client.chat_postMessage(
        channel=target,
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": '```This ticket has not had a public comment in 7 days. Please provide an update or close '
                            'the ticket if solved!.```\n\n\n '
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": '\n' '\n' '<' + zenURL + '|' + zenSubject + '>'
                },
                "accessory": {
                    "type": "image",
                    "image_url": "https://cdn2.iconfinder.com/data/icons/calendar-rounded/512/xxx048-512.png",
                    "alt_text": "Your Text Here"
                }
            },
        ]
    )
