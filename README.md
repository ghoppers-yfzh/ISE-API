[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/wukong-sun/ISE-API)
# What is this?
Multiple function script for polling data from ISE database for certain information.(Network Device, Endpoint, Endpoint Group .etc)
![ISE-API](/ISE-API-flow.png)

## Installation

#### 1. Clone the repo
git clone https://github.com/wukong-sun/ISE-API.git
#### 2. change into directory
cd ISE-API
#### 3. Create the virtual environment in a sub dir in the same directory
python3 -m venv venv
#### 4. Start the virtual environment and install requirements.txt from the <ISE-API>
./venv/bin/activate.bat

pip install -r requirements.txt 
      
## Functions and Run result
Several funcations/API included in this script

#### CLI RUN
python3 ISEAPI.py

1. Function for polling the Endpoint device Group and UUID
![endpointgrouplist](/endpointgrouplist.png)
2. Function for polling the endpoint group details
![endpointgroupdetail](/endpointgroupdetail.png)
3. Function for polling the endpoint details and print out the group name
![endpointdetail](/endpointdetail.png)
4. Function for polling a network device detail
![networkdevicedetail](/networkdevicedetail.png)

### Keep working on this script to include more features and easier to use.

## License
This project is licensed under the BSD 2-Clause "Simplified" License - see the  [LICENSE](./LICENSE) file for details.

