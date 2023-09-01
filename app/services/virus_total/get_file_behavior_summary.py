from app.config.instances import virustotal_instance as instance
import requests

def get_file_behavior_summary(hash_value: str) -> dict:

        """
        Retrieve the behavior summary for a file identified by a given hash value from the VirusTotal database.

        This function performs an HTTP GET request to the VirusTotal API to fetch the behavior summary
        of a file identified by its hash value.

        Parameters:
        hash_value (str): The hash value to query. Should be a valid SHA-256, SHA-1, or MD5 hash.

        Returns:
        dict: A dictionary containing the behavior summary if the query is successful.

        Raises:
        None: This function handles exceptions and returns an error message in the dictionary.

        """

        response = requests.get(f"{instance.API_URL}/files/{hash_value}/behaviour_summary", headers=instance.auth_headers)
    
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {"error": "Failed to get file behavior summary from VirusTotal."}