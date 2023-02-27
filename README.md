# GooBox Microservice Honeypot
## Structure
GooBox consists of 5 containers: api, auth, nginx, db, frontend.
<img width="841" alt="Screen Shot 2023-02-26 at 5 46 11 PM" src="https://user-images.githubusercontent.com/91851888/221453247-6211acef-dc36-433d-9ebd-6ece59b425a1.png">
<br>
The api container handles all the paste logic. The auth container handles all the authentication logic. The db container stores all paste and authentication data. NGINX proxies requests to either the api or auth. Frontend container contains the react app.
## Hosting
GooBox is hosted on msa.seclab.cs.ucsb.edu on k3s. There are NodePorts exposed for NGINX, frontend and kiali. Check the services in Kubernetes to find the exact port.
<br>
Kiali, the monitoring page, can only be accessed via VPN or on seclab wifi. It is on http://msa.seclab.cs.ucsb.edu:31822/kiali.
## Deployment
SSH into user@msa.seclab.cs.ucsb.edu. Delete any old deployment/service/persistent volume claim of the application. Reapply the goo-box.yaml file.
