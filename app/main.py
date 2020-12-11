#import section - using bare minimum require libs - flask , request , Response and json
from flask import Flask, request, Response
import json

#dictionary object to store the max cpu and max mem for an ip
in_mem={}

#create app object and define app routes
app = Flask(__name__)

@app.route('/metrics',methods=['POST'])
def metrics():#method to store cpu and mem consumptions via post method from multiple ip end points
	
	try:
	
		#store metrics
		json_data=json.loads(request.data.decode('utf-8'))

		percentage_cpu_used= json_data['percentage_cpu_used']
		percentage_memory_used=json_data['percentage_memory_used']
		ip_address=request.remote_addr
		print("percentage_cpu_used",percentage_cpu_used,"percentage_memory_used",percentage_memory_used,"ip",ip_address) #logging data to test entries
		
		if(ip_address in in_mem):#check if the ip is new or there is a previous entry of cpu/mem for the ip
			cur_cpu=in_mem[ip_address]['percentage_cpu_used']
			cur_mem=in_mem[ip_address]['percentage_memory_used']
			if(percentage_cpu_used>cur_cpu):
				in_mem[ip_address]['percentage_cpu_used']=percentage_cpu_used
			if(percentage_memory_used>cur_mem):
				in_mem[ip_address]['percentage_memory_used']=percentage_memory_used
		else:#for new ip sore the current cpu/mem as a max only
			in_mem[ip_address]={'percentage_cpu_used':percentage_cpu_used,"percentage_memory_used":percentage_memory_used}	
		
		status_code = Response(status=200)	
		return(status_code)
	except:
		status_code = Response(status=500)
		return(status_code)	
		
@app.route('/report',methods=['GET'])
def report():
	print(in_mem)
	return(json.dumps(in_mem))

if __name__ == '__main__':
	app.run(host='0.0.0.0')
