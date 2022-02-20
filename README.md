# usefulContainers
Contains containers useful for testing and learning exercises.

## meuApache
This is just Apache httpd, but it listens on port 9000 and it shows a one-liner greeting. It is meant to test containers and container orchestrators. You launch it with a given name and port, then try to reach it.  
As of now it only listens in port 9000. But I plan to make that a parameter.    
  
To run it as a standalone docker container: `docker container run --rm --network=host --detach jrkessl/meuapache`  
  
## meuCurl
Just a simple container that extracts a webpage from a parametized URL and port, outputs it to the std output, then exits.  
Useful for testing network connectivity, and network routing when learning container orchestrators: launch a webpage somewhere with some port, and use this container to try to reach it.   
You may be thinking "I can just run curl in my prompt, why do I need this" but think you want to test container to container communication, and not host to container communication.  

Run as: `docker container run --rm --env HOS=localhost --env POR=9000 --network=host jrkessl/meucurl`
