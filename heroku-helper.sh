#!/bin/bash

set -e

function updateVersion(){
  VERSION=$(cat $1)
  echo "VERSION: ${VERSION}"

  curl -S -n -X PATCH https://api.heroku.com/apps/${HEROKU_APP}/config-vars \
    -d "{ \"VERSION\":\"${VERSION}\" }" \
    -H "Content-Type: application/json" \
    -H "Accept: application/vnd.heroku+json; version=3" \
    -H "Authorization: Bearer ${HEROKU_DEV_KEY}" > /dev/null
}

function loginHeroku(){
  echo "machine api.heroku.com
  login $1
  password $2
machine git.heroku.com
  login $1
  password $2
  " > ~/.netrc
}

function deployMaster(){
  echo "Setup app remote..."
  heroku git:remote -a $1
  echo "Deploying current branch to heroku master..."
  git push heroku $(git subtree split --prefix $2 HEAD):master --force
}
