from app.config.instances import virustotal_instance as instance
import requests

def get_domain_report(tld: str) -> dict:

        """
        Retrieve the domain report for a given top-level domain (TLD) from the VirusTotal database.

        This function performs an HTTP GET request to the VirusTotal API to fetch the domain report
        for a specified TLD.

        Parameters:
        tld (str): The top-level domain to query.

        Returns:
        dict: A dictionary containing the domain report if the query is successful.
        Raises:
        None: This function handles exceptions and returns an error message in the dictionary.

        """
        response = requests.get(f"{instance.API_URL}domains/{tld}", headers=instance.auth_headers)
        
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {"error": "Failed to get domain report from VirusTotal."}