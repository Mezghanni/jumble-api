# Build locally
```bash
python3 -m venv ../my-venv
source ../my-venv/bin/activate
pip install -r requirements.txt
```

# Run locally

```bash
uvicorn app.main:app --reload
```
Go to this page http://127.0.0.1:8000/docs to test based on OpenAPI client.

# Run tests locally
```bash
pip install -r requirements_tests.txt
pytest test
```

# Docker build 
```bash
 docker build ./ -t jumble-api:0.0.1
 ```

# Docker run
```bash
docker run -p 8000:80  jumble-api:0.0.1
```
Go to this page http://127.0.0.1:8000/docs to test based on OpenAPI client.

# Deploy this API server to a local orchestration platform (minikube / minishift)

```bash
helm upgrade --install jumble-api ./jumble-api-chart
```

To access the application you need to do a port forward based on the following script
```bash
export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=jumble-api-chart,app.kubernetes.io/instance=jumble-api" -o jsonpath="{.items[0].metadata.name}")
export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
echo "Visit http://127.0.0.1:8080/docs to use your application"
kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```