#!/bin/sh
docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD
if [ "$TRAVIS_BRANCH" = "master" ]; then
    TAG="latest"
else
    TAG="$TRAVIS_BRANCH"
fi

docker build -f Dockerfile -t $DOCKER_USERNAME/$REPO_NAME:$TAG .
docker push $DOCKER_USERNAME/$REPO_NAME