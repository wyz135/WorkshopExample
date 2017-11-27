#!/usr/bin/env bash

if [ "$TRAVIS_PULL_REQUEST" != "false" -o "$TRAVIS_BRANCH" != "master" ]; then
    echo "Not on master branch, nor pull request. Not building doco"
    exit 0;
fi

if [ -n "$GITHUB_API_KEY" ]; then
    echo "Github key found. Building documentation."
    cd "$TRAVIS_BUILD_DIR"/doc
    make clean
    make html
    if [ "$TRAVIS_PYTHON_VERSION" != "3.6" ]; then
        cd "$TRAVIS_BUILD_DIR"
        rm -rf .git/
        cd doc/_build/html
        git config --global user.email "travis"
        git config --global user.name "travis"
        # Create the nojekyll file so Github doesnt try to build for us
        touch .nojekyll
        git init
        git add .
        echo "Committing Github Pages"
        git commit -m init
        # Make sure to make the output quiet, or else the API token will leak!
        # This works because the API key can replace your password.
        echo "Pushing"
        git push -f -q "https://${GITHUB_API_KEY}@${GH_REF}" master:gh-pages  > /dev/null 2>&1 && echo "Pushed"
    fi
fi
echo "Deploy script ending"