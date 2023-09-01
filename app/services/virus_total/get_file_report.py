from app.config.instances import virustotal_instance as instance
import requests

def get_file_report(id: str) -> dict:
 
        """
        Retrieve the file report for a file identified by a given hash value or ID from the VirusTotal database.

        This function performs an HTTP GET request to the VirusTotal API to fetch the file report
        of a file identified by its hash value or ID.

        Parameters:
        id (str): The hash value or ID to query. Should be a valid SHA-256, SHA-1, MD5 hash, or a specific VirusTotal ID.

        Returns:
        dict: A dictionary containing the file report if the query is successful.

        Raises:
        None: This function handles exceptions and returns an error message in the dictionary.

        """

        response = requests.get(f"{instance.API_URL}files/{id}", headers=instance.auth_headers)
        
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {"error": "Failed to get data with hash provided to VirusTotal."}