from app.config.instances import hybridanalysis_instance as instance
import app.services.hybrid_analysis.search_hash as sh
import requests
import json

def memory_hex_dump(sha256: str) -> dict:
        
        """  
        Retrieve the hex dump of the memory for a given SHA256 hash from the Hybrid Analysis database.

        ***Note: This function requires a verified API key from Hybrid Analysis to work.

        Parameters:
        sha256 (str): The SHA256 hash of the file to query.

        Returns:
        dict: A dictionary containing the hex dump if the query is successful.

        Raises:
        None: This function handles exceptions and returns an error message or a string.

        """

        # search hash function provides the job_id if it exists.    

        search_hash = sh.search_hash(sha256)

        # Access the 'job_id' key-value pair
        job_id = search_hash[0].get('job_id')
        
        if job_id == None:
            return "Job does not exist for this hash, no memory dump to return."
        
        response = requests.get(f"{instance.API_URL}/report/{job_id}/memory-dump/hex-dump?filename=mem_dump.mem", headers=instance.auth_headers)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {"error": "Failed to get memory dump report from Hybrid Analysis."}