#!/bin/sh
docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD
if [ "$TRAVIS_BRANCH" = "master" ]; then
    TAG="latest"
else
    TAG="$TRAVIS_BRANCH"
fi

REPO = ccid-buzz
# docker build -f Dockerfile -t $TRAVIS_REPO_SLUG:$TAG .
docker build -f Dockerfile -t $DOCKER_USERNAME/$REPO:$TAG .
# docker push $TRAVIS_REPO_SLUG
docker push $DOCKER_USERNAME/${PROJECT}