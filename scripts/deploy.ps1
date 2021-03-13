kubectl apply --record -f .\k8s\secrets.yaml
kubectl apply --record -f .\k8s\deployment.yaml --validate=false