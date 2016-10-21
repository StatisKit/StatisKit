set +xe

DEFAULT_DOCKER_TAGS="14.04 16.04"

if [[ -z $DOCKER_TAGS ]]; then
    DOCKER_TAGS=$DEFAULT_DOCKER_TAGS;
else
    echo "Tags to build: "$DOCKER_TAGS;
fi

if [[ -z $DOCKER_CHANNEL ]]; then
    DOCKER_CHANNEL="statiskit";
else
    echo "Using docker channel: "$DOCKER_CHANNEL;
fi

for DOCKER_TAG in DOCKER_TAGS; do
    docker pull ubuntu:$DOCKER_TAG
    docker tag ubuntu:DOCKER_TAG ubuntu
    docker build -t DOCKER_CHANNEL/ubuntu:DOCKER_TAG .
done