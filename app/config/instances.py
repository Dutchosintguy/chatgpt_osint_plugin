# app/config/instances.py

from .configuration import MalwareBazaarAPI, VirusTotalAPI, HybridAnalysisAPI

malwarebazaar_instance = MalwareBazaarAPI()
virustotal_instance = VirusTotalAPI()
hybridanalysis_instance = HybridAnalysisAPI()