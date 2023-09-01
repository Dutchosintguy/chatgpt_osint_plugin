from dotenv import load_dotenv
import os

class Configuration:
    """
    Base class for Configuration.

    This class is intended to be subclassed by specific API configurations.
    """
    def __init__(self):
        """Initialize the Configuration class."""
        pass


class MalwareBazaarAPI(Configuration):
    """
    Configuration class for MalwareBazaar API.

    This class inherits from the Configuration class and sets up the API key, API URL, and authentication headers
    for the MalwareBazaar API.
    """
    def __init__(self):
        """Initialize the MalwareBazaarAPI class."""
        load_dotenv()
        self.API_KEY = os.getenv('MALWARE_BAZAAR_API_KEY')
        self.API_URL = os.getenv('MALWARE_BAZAAR_API_URL')
        self.auth_headers = {'API-KEY': self.API_KEY }


class VirusTotalAPI(Configuration):
    """
    Configuration class for VirusTotal API.

    This class inherits from the Configuration class and sets up the API key, API URL, and authentication headers
    for the VirusTotal API.
    """
    def __init__(self):
        """Initialize the VirusTotalAPI class."""
        load_dotenv()
        self.API_KEY = os.getenv('VIRUS_TOTAL_API_KEY')
        self.API_URL = os.getenv('VIRUS_TOTAL_API_URL')
        self.auth_headers = {'x-apikey': self.API_KEY}


class HybridAnalysisAPI(Configuration):
    """
    Configuration class for Hybrid Analysis API.

    This class inherits from the Configuration class and sets up the API key, API URL, and authentication headers
    for the Hybrid Analysis API.
    """
    def __init__(self):
        """Initialize the HybridAnalysisAPI class."""
        load_dotenv()
        self.API_KEY = os.getenv('HYBRID_ANALYSIS_API_KEY')
        self.API_URL = os.getenv('HYBRID_ANALYSIS_URL')
        self.auth_headers = {'api-key': self.API_KEY,
                             'user-agent': 'Falcon Sandbox'
                             }