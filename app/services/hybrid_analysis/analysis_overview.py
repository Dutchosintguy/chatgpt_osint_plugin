from app.config.instances import hybridanalysis_instance as instance
import requests

def analysis_overview(sha256: str):
 
        """
        Retrieve the analysis overview for a given SHA256 hash from the Hybrid Analysis database.

        This function performs an HTTP GET request to the Hybrid Analysis API to fetch the analysis overview
        of a file identified by its SHA256 hash.

        Parameters:
        sha256 (str): The SHA256 hash of the file to query.

        Returns:
        dict: A dictionary containing the analysis overview if the query is successful. Otherwise, a dictionary
            containing an error message.
            
        Raises:
        None: This function handles exceptions and returns an error message in the dictionary.

        """
        response = requests.get(f"{instance.API_URL}overview/{sha256}", headers=instance.auth_headers)
        
        what = f"{instance.API_URL}/overview/{sha256}"

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {"error": "Failed to get sha256 report from Hybrid Analysis."}