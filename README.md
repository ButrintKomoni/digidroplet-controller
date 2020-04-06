# digidroplet-controller
DigitalOcean API Controller



## Installing dependencies

You can install the required dependecies using **pip**

    pip3 install -r requirements.txt


## Configuration

Put the API key created from DigitalOcean to the token param on the conf.cfg file 

    [auth]
    token = 79tiw3gimvg9t9sspe2pj9vd74dxk9lspoftwhct0m7uk4yzqa6r447smrid9lsp
    
## Usage 

  Get the current status of the droplets running using the --status argument
  
          17:31:06 butrint@void.local droplet-api master python3 digidroplet.py --status 
          DROPLET: void.international, STATUS:ACTIVE, IP:x.x.x.x, REGION: NYC1, DIST: debian-x64


    
## TODO

Create the 
         
         - shutdown function 
         
         - add ssh keys function
         
         - add domain to network function
         
         - restart function
         
         - drop
         
         - run the droplet function
