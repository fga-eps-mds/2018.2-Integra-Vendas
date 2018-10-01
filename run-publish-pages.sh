echo "GH_NAME=${GH_NAME}" >> docs/.env
echo "GH_EMAIL=${GH_EMAIL}" >> docs/.env
echo "GH_TOKEN=${GH_TOKEN}" >> docs/.env
docker run -v `pwd`:"/app" -w "/app" --env-file docs/.env lucascst/gh-pages-docker-travis bash -c "cd docs; sh publish.sh"
rm -rf docs/.env