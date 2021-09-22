# Grafana Plugins Init Container

This repository contains an init container image that is used by the Grafana Operator to install additional plugins.

## Building

To build and push the image run:

```sh
make image/build
make image/push
```

## Develop locally

To test that the python script works you need to set a environment variable.

```shell
export GRAFANA_PLUGINS="grafana-clock-panel:1.0.1,grafana-simple-json-datasource:1.3.5"
```
