#!/bin/bash

helm upgrade --install \
	--debug \
	--kube-context $(kubectl config current-context) \
	--version 4.0.0 \
	--namespace monitoring \
	--values values.yaml \
	--recreate-pods \
	grafana stable/grafana
