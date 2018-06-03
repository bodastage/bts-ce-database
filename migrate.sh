#!/bin/bash
#
# 

set -x 

basefolder=$(realpath $(dirname $0))

cd $basefolder

alembic upgrade head
