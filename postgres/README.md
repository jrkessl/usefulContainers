# Postgres in k8s with local persistent volume, hostPath type
This demonstrates creating a Kubernetes persistent volume, hostPath type, and the persistent volume claim that is required to bind this to a pod (in this case, a Postgres deployment).  
Remember: hostPath volume type creates a volume stored on the node, good for testing; in production, use a network backed-volume, such as an EBS-backed volume in AWS.  
## Creation
These steps demonstrate creation of the volume and deployment. 
1. Create the path in the host (in the k8s node):  
`sudo mkdir /home/ubuntu/persistent-volume`
2. Create a persistent volume for the Postgres deployment.  
Specs are in the file mentioned below. It creates a 1 GB persistent volume named `persistent-volume-meupostgres`.  
`kubectl apply -f persistent-volume-postgres.yml`
3. Inspect the volume with command below. The volume should be in status "available".  
`kubectl get persistentvolume/persistent-volume-meupostgres`
4. Create a persistent volume claim.  
The persistent volume claim is required to bind the volume to the pod. The claim will (naturally) claim the volume, and the pod will consume the claim like if the claim was the volume itself.  
Check specs in the file mentioned below. This file creates a claim named `pv-claim-postgres`:  
`kubectl apply -f volume-claim-postgres.yml`
5. Verify the created claim:  
`kubectl get persistentvolumeclaim/pv-claim-postgres`
6. If you check the persistent volume again with the command from step 3 you will see it is now in status "bound". 
7. Launch the Postgres deployment using this persistent volume with:  
`kubectl apply -f deployPostgres.yml`
## Verification  
These steps demonstrate verifying how the solution was correctly applied:  
1. Test this Postgres deployment that uses persistent volumes:  
Get the IP of the Postgres load balancer: `kubect get all`  
Log in the Postgres database:  
`docker container run -it --rm postgres psql -U postgres -h <IP of Posgres load balancer from step above>`  
Tip: Postgres password is in the yml file that created the Deployment.  
Now, into this Postgres database, create some table:  
```
CREATE TABLE t1 (
    nome varchar (30) NOT NULL
);
INSERT INTO T1 ( NOME ) VALUES ( 'zezinho' );
SELECT * FROM T1;
```
2. Now delete this deployment: `kubect delete -f deployPostgres.yml`  
3. Observe how the Postgres files remain in the local path of the volume: `sudo ls /home/ubuntu/persistent-volume`  
4. Re-launch the deployment (notice the volume is not affected, since it was created from another yml file):  
`kubectl apply -f deployPostgres.yml`  
5. Log into Postgres and notice how the table is still there. Repeat step 1 and then do `select * from t1;`

