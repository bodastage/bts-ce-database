#!/bin/bash
#
# 

basefolder=$(realpath $(dirname $0))

cd $basefolder

alembic upgrade head
