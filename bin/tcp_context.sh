#!/bin/sh

name="rootless"
description="Rootless mode"
host="tcp://0.0.0.0:2376"

~/bin/docker --context=default context rm -f "${name}"
~/bin/docker --context=default context create "${name}" --docker "host=${host}" --description "${description}"
~/bin/docker --context=default context use "${name}" > /dev/null
