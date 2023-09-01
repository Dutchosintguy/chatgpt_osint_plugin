from app.config.instances import hybridanalysis_instance as instance
import requests

def search_hash(hash_value: str):
 
        """
        Search for a given hash value in the Hybrid Analysis database.

        This function performs an HTTP POST request to the Hybrid Analysis API to search for information
        related to a file identified by its hash value.

        Parameters:
        hash_value (str): The hash value to search for. Should be a valid SHA-256, SHA-1, or MD5 hash.

        Returns:
        dict: A dictionary containing the search results if the query is successful. Otherwise, a dictionary
            containing an error message.

        Raises:
        None: This function handles exceptions and returns an error message in the dictionary.

        """

        payload = { 
             'hash':hash_value
        }

        response = requests.post(f"{instance.API_URL}/search/hash", headers=instance.auth_headers, data=payload)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {"error": "Failed to get data with hash provided to Hybrid Analysis."}