#!/usr/bin/env bash

## NOTE: These functions are entirely unreviewed for fitnes for any purpose.

function shell_escape_single {
    # shell_escape_single()
    local strtoescape=${1}
    local output="$(echo "${strtoescape}" | sed "s,','\"'\"',g")"
    echo "'"${output}"'"
}
