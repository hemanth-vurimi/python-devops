import docker

client = docker.from_env()

def list_containers():
    containers = client.containers.get()
    for container in containers:
        print(container.name)

list_containers()