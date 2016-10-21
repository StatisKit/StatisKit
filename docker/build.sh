set +xe

DEFAULT_DOCKER_BUILD_TAGS="14.04 16.04"

if [[ -z $DOCKER_BUILD_TAGS ]]; then
    DOCKER_BUILD_TAGS=$DEFAULT_DOCKER_BUILD_TAGS;
else
    echo "Tags to build: "$DOCKER_BUILD_TAGS;
fi

if [[ -z $DOCKER_CHANNEL ]]; then
    DOCKER_CHANNEL="statiskit";
else
    echo "Using docker channel: "$DOCKER_CHANNEL;
fi

for DOCKER_BUILD_TAG in DOCKER_BUILD_TAGS; do
    docker pull ubuntu:$DOCKER_BUILD_TAG
    docker tag ubuntu:DOCKER_BUILD_TAG ubuntu
    docker build -t DOCKER_CHANNEL/ubuntu:DOCKER_BUILD_TAG .
done