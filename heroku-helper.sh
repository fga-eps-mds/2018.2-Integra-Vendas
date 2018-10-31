VERSION=$(cat ./api/VERSION)
# echo ${VERSION}

curl -S -n -X PATCH https://api.heroku.com/apps/${HEROKU_APP}/config-vars \
  -d "{ \"VERSION\":\"${VERSION}\" }" \
  -H "Content-Type: application/json" \
  -H "Accept: application/vnd.heroku+json; version=3" \
  -H "Authorization: Bearer ${HEROKU_DEV_KEY}" > /dev/null
