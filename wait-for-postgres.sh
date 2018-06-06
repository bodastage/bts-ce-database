#!/bin/bash
# wait-for-postgres.sh

set -e

cmd="$@"

until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$POSTGRES_PASSWORD" -U "postgres" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd