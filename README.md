# airmeet_sre_challenge
This repo contains the problem statement and solution of Airmeet SRE hiring. !  
Repo contains rest api made with python flask &lt;3 and dockerfile to build the container that exposes api via docker container.


Steps to implement :

1. Install docker - for detailed instruction refer <https://docs.docker.com/engine/install/>
2. git clone https://github.com/zerocool443/airmeet_sre_challenge
3. mv airmeet_sre_challenge
4. build -t airmeet_challenge:latest . (Build the docker image using dockerfile)
5. docker run -d -p 8080:5000 airmeet_challenge:latest (run the docker container that exposes port 8080 to interact with api)

Steps to test api :


#Test /metrics 
#below command can be executed from multiple host that have reacability to server exposing docker container on port 8080

curl -XPOST -H "Content-Type: application/json"​ --data '{"percentage_cpu_used": 10, "percentage_memory_used": 10}' http://127.0.0.1:8080/metrics

#Test /report 

curl -X GET http://127.0.0.1:8080/report


