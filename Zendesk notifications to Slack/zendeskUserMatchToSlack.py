# Instructions on how to lookup the ZENDESK USER ID:
# https://support.zendesk.com/hc/en-us/articles/360021164293-Is-there-a-user-id-that-is-not-the-user-email-address-

# Instructions on how to lookup the SLACK USER ID:
# https://help.workast.com/hc/en-us/articles/360027461274-How-to-find-a-Slack-user-ID

# uncomment and add to elif statements if you require more ID's to be looked up
# copy elif statements if you require more ID's then placeholders
# the else statement should return back to implementor of script to check for errors

# custom function that returns the matching SLACKID of a ZENDESKID that is passed to it.
def slackUserLookup(zenAssignee):
    # zendesk = FIRST.LASTNAME ##add the Zendesk full name here for record keeping
    if zenAssignee == 12345678:  # zendesk user ID
        # slack = FIRST.LASTNAME ##add the SLACK full name here for record keeping
        return 'U12345678'
    # zendesk = FIRST.LASTNAME
    # elif zenAssignee == 12345678:
    #    return 'U12345678'
    # slack = FIRST.LASTNAME
    # elif zenAssignee == 12345678:
    # zendesk = FIRST.LASTNAME
    #    return 'U12345678'
    # slack = FIRST.LASTNAME
    # elif zenAssignee == 12345678:
    # zendesk = FIRST.LASTNAME
    #    return 'U12345678'
    # slack = FIRST.LASTNAME
    else:
        return 'U12345678'

# print(slackUserLookup('360197014496'))
