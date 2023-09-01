from app.config.instances import virustotal_instance as instance
import requests

def get_ip_report(ip_address: str) -> dict:
 
        """
        Retrieve the report for an IP address from the VirusTotal database.

        This function performs an HTTP GET request to the VirusTotal API to fetch the report
        related to a specified IP address.

        Parameters:
        ip_address (str): The IP address to query. Should be a valid IPv4 or IPv6 address.

        Returns:
        dict: A dictionary containing the IP address report if the query is successful.
        
        Raises:
        None: This function handles exceptions and returns an error message in the dictionary.

        """

        response = requests.get(f"{instance.API_URL}ip_addresses/{ip_address}", headers=instance.auth_headers)
        
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {"error": "Failed to get IP address to VirusTotal API."}