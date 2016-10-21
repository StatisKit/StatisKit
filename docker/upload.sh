set +xe

DEFAULT_DOCKER_UPLOAD_TAGS="14.04 16.04"

if [[ -z $DOCKER_UPLOAD_TAGS ]]; then
    DOCKER_UPLOAD_TAGS=$DEFAULT_DOCKER_UPLOAD_TAGS;
else
    echo "Tags to upload: "$DOCKER_UPLOAD_TAGS;
fi

if [[ -z $DOCKER_USERNAME ]]; then
    read -p "Username: " DOCKER_USERNAME;
else
    echo "Username: "$DOCKER_USERNAME;
fi

if [[ -z $DOCKER_PASSWORD ]]; then
    read -s -p $DOCKER_USERNAME"'s password: " DOCKER_PASSWORD;
else
    echo $DOCKER_USERNAME"'s password: [secure]";
fi

if [[ -z $DOCKER_CHANNEL ]]; then
    DOCKER_CHANNEL="statiskit";
else
    echo "Using docker channel: "$DOCKER_CHANNEL;
fi

set +x

docker login -u="$DOCKER_USERNAME" -p="$DOCKER_PASSWORD"
if [ $? -ne 0 ]; then
    exit 1;
fi

set -x

for DOCKER_UPLOAD_TAG in $DOCKER_UPLOAD_TAGS; do
    docker push $DOCKER_UPLOAD_CHANNEL/ubuntu:$DOCKER_UPLOAD_TAG
done

docker logout

set +x