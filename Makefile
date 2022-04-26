ORG=grafana-operator
PROJECT=grafana_plugins_init
REG=quay.io
TAG=0.0.6
PKG=github.com/grafana-operator/grafana_plugins_init

.PHONY: image/build
image/build:
	docker build -t ${REG}/${ORG}/${PROJECT}:${TAG} .

# Build and push a multi-architecture docker image
.PHONY: image/buildx
image/buildx:
	docker buildx build --platform linux/amd64,linux/arm64,linux/s390x,linux/ppc64le --push -t ${REG}/${ORG}/${PROJECT}:${TAG} .

.PHONY: image/push
image/push:
	docker push ${REG}/${ORG}/${PROJECT}:${TAG}
