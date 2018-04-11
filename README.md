# Lab 0


## run python flask locally
```
git clone https://github.com/enghwa/ecs-pyflask.git

cd ecs-pyflask

sudo pip install -r requirements.txt

python app.py

curl http://localhost:8080/
```

##  docker build and run locally


```
docker build -t pyflask .
docker images


docker run -it -p5000:5000 pyflask:latest

curl http://localhost:5000/

```

## login to AWS ECR and create a repository

```
`aws ecr get-login --no-include-email`

aws  ecr create-repository --repository-name pyflask

# copy the repositoryUri - ????????????.dkr.ecr.ap-southeast-1.amazonaws.com/pyflask

 docker tag pyflask:latest ???????????.dkr.ecr.ap-southeast-1.amazonaws.com/pyflask:v1
 docker push  ???????????.dkr.ecr.ap-southeast-1.amazonaws.com/pyflask:v1

```


# Lab 1

https://aws.amazon.com/getting-started/container-microservices-tutorial/

- Module One - Containerize the Monolith  https://aws.amazon.com/getting-started/container-microservices-tutorial/module-one/
- Module Two - Deploy the Monolith https://aws.amazon.com/getting-started/container-microservices-tutorial/module-two/
- Module Three - Break the Monolith https://aws.amazon.com/getting-started/container-microservices-tutorial/module-three/
- Module Four - Deploy Microservices https://aws.amazon.com/getting-started/container-microservices-tutorial/module-four/
- Module Five - Clean Up https://aws.amazon.com/getting-started/container-microservices-tutorial/module-five/

 
