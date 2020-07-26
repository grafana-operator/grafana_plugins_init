ORG=integreatly
PROJECT=grafana_plugins_init
REG=quay.io
TAG=0.0.3
PKG=github.com/integr8ly/grafana_plugins_init

.PHONY: image/build
image/build:
	docker build -t ${REG}/${ORG}/${PROJECT}:${TAG} .

.PHONY: image/push
image/push:
	docker push ${REG}/${ORG}/${PROJECT}:${TAG}
