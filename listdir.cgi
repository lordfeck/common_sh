#!/bin/bash

# List the contents of a directory to a web user.
# Author: Thran Authored: 29-04-2020

. common.sh
listDir="/etc/"

writeHeader "Server: Etc Directory Listing"

wH "Files available:"
writeList $(ls $listDir)

wP '<a href="../index.html">Return to homepage</a>'

writeFooter
