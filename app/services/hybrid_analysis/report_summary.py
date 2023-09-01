from app.config.instances import hybridanalysis_instance as instance
import app.services.hybrid_analysis.search_hash as sh
import requests

def report_summary(sha256: str) -> dict:
        
        """
        Retrieve the report summary for a given SHA256 hash from the Hybrid Analysis database.

        This function first performs a search operation to retrieve the job ID associated with the given SHA256 hash.
        It then performs an HTTP GET request to fetch the report summary.

        Parameters:
        sha256 (str): The SHA256 hash of the file to query.

        Returns:
        dict: A dictionary containing the report summary if the query is successful.

        Raises:
        None: This function handles exceptions and returns an error message or a string.

        """
        
        # must retrieve information about the hash in order to populate report IDs to run the operations below.

        search_hash = sh.search_hash(sha256)

        # Access the 'job_id' key-value pair
        job_id = search_hash[0].get('job_id')

        if job_id == None:
            return "Job does not exist for this hash, no memory dump to return."
        
        response = requests.get(f"{instance.API_URL}/report/{job_id}/summary", headers=instance.auth_headers)

        print(response.content)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {"error": "Failed to get memory dump report from Hybrid Analysis."}