from app.config.instances import hybridanalysis_instance as instance
import app.services.hybrid_analysis.search_hash as sh
import requests

def memory_strings_dump(sha256: str):
        
        """
        Retrieve the strings extracted from the memory of a given SHA256 hash from the Hybrid Analysis database.

        ***Note: This function requires a verified API key from Hybrid Analysis to work.

        This function first performs a search operation to retrieve the job ID associated with the given SHA256 hash.
        It then performs an HTTP GET request to fetch the strings extracted from the memory.

        Parameters:
        sha256 (str): The SHA256 hash of the file to query.

        Returns:
        dict or str: A dictionary containing the extracted strings if the query is successful. Otherwise, a dictionary
                    containing an error message or a string indicating that the job does not exist.

        Raises:
        None: This function handles exceptions and returns an error message or a string.
        
        """

        # must retrieve information about the hash in order to populate report IDs to run the operations below.

        search_hash = sh.search_hash(sha256)

        # Access the 'job_id' key-value pair
        job_id = search_hash[0].get('job_id')

        if job_id == None:
            return "Job does not exist for this hash, no memory dump to return."
        
        response = requests.get(f"{instance.API_URL}/report/{job_id}/memory-dump/extracted-strings?filename=mem_strings_dump.mem", headers=instance.auth_headers)
        
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {"error": "Failed to get memory dump report from Hybrid Analysis."}