# cbpi-whitelist

This plugin allows you to customise the ips that can access the cbpi ui

## Setup
By default this plugin whitelists `127.0.0.1` and your local network cidr. e.g. `192.168.1.68` will be caught by the automatically generated cidr of `192.168.1.1/24`. You can add more cidr's to the list by adding them to the settings under `custom_cidrs`, this should be a comma seperated list of cidrs. 

If you want to whitelist a full iip range e.g. 10.128.0.1 to 10.128.0.254 the cidr would be 10.128.0.1/24. To specify a specific ip range it would be 10.128.0.1/32

## Notes
This plugin will work in conjunction with the httpauth plugin, the ip's will be validated before the auth plugin is called. This can be used for an extra level of security

## Viewing blocked ips
There is an api endpoint on `/api/blockedips` that will show all the ips that have been blocked by this plugin. This is helpful when finding ip's that you may want to unblock


## TODO
I am currently investigating a way to do request origin whitelisting so that things like incoming webhooks can be secured. ie. plaato, tiltpi etc
