APP_NAME=devops-case
CHART_PATH=charts/devops-case
VALUES_DEV=$(CHART_PATH)/values-dev.yaml

status:
	kubectl get nodes
	kubectl get pods
	helm list

deploy:
	helm upgrade --install $(APP_NAME) $(CHART_PATH) -f $(VALUES_DEV)

rollback:
	helm rollback $(APP_NAME)

history:
	helm history $(APP_NAME)

logs:
	kubectl logs -l app.kubernetes.io/name=$(APP_NAME) --tail=100

restart:
	kubectl rollout restart deployment/$(APP_NAME)

rollout:
	kubectl rollout status deployment/$(APP_NAME)

grafana:
	kubectl port-forward --address 0.0.0.0 -n monitoring svc/monitoring-grafana 3001:80

prometheus:
	kubectl port-forward --address 0.0.0.0 -n monitoring svc/monitoring-kube-prometheus-prometheus 9090:9090

test:
	curl -H "Host: devops-case.local" http://$$(minikube ip)/ping
