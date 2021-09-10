Common.sh Bash JSON composer
=====================

Yes, this exists. Yes, this works.

Tested with FastCGI on NGINX.

## USAGE
Run jsonstats.cgi to get a printout of system stats.

## USING ELSEWHERE
Do a call to `source common.sh` and call the relevant functions to print the lines of JSON.

## USAGE SUGGESTIONS
Ideal for private networks where you want a quick glance of system stats.

It can run anything your shell can run, so I'd caution against anything public-facing; this hasn't been audited for security and likely will never be.

## BONUS
There is also basic support for generating HTML! See `listdir.cgi` for sample code.

