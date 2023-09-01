from fastapi import APIRouter
import app.utils.num_tokens_from_string as strtkn
import app.services.virus_total.get_ip_report as gir
import app.services.virus_total.get_file_report as gfr
import app.services.virus_total.get_domain_report as gdr
import app.services.virus_total.get_file_behavior_summary as fbs

router = APIRouter()

@router.post("/get-ip-report", description="Get IP report from VirusTotal.")

async def get_ip_report(ip_address: str) -> dict:

    """
    Retrieve the IP report for a given IP address from the VirusTotal database.

    Parameters:
    ip_address (str): The IP address to query.

    Returns:
    dict: The IP report from VirusTotal.

    Raises:
    HTTPException: If the query to VirusTotal fails for any reason.

    """
    response = gir.get_ip_report(ip_address)
    return response

@router.post("/get-file-report", description="Get file report from VirusTotal using sha256, md5, or sha1 hashes.")

async def get_file_report(id: str) -> dict:   
    """
    Retrieve the file report for a given hash (SHA-256, MD5, or SHA-1) from the VirusTotal database.

    Parameters:
    id (str): The hash value to query.

    Returns:
    dict: The file report from VirusTotal.

    Raises:
    HTTPException: If the query to VirusTotal fails for any reason.

    """
    response = gfr.get_file_report(id)
    return response

@router.post("/get-domain-report", description="Get domain report from VirusTotal.")

async def get_domain_report(tld: str) -> dict:

    """
    Retrieve the domain report for a given top-level domain (TLD) from the VirusTotal database.

    Parameters:
    tld (str): The top-level domain to query.

    Returns:
    dict: The domain report from VirusTotal.

    Raises:
    HTTPException: If the query to VirusTotal fails for any reason.

    """
    response = gdr.get_domain_report(tld)
    return response

@router.post("/get-file-behavior-summary", description="Get file behavior summary from VirusTotal.")

async def get_file_behavior_summary(hash_value: str) -> dict:

    """
    Retrieve the file behavior summary for a given hash from the VirusTotal database.

    Note: The response is often too large and may be truncated.

    Parameters:
    hash_value (str): The hash value to query.

    Returns:
    dict: The file behavior summary from VirusTotal, possibly truncated.

    Raises:
    HTTPException: If the query to VirusTotal fails for any reason.

    """

    response = fbs.get_file_behavior_summary(hash_value)
    
    #print(strtkn.num_tokens_from_string(str(response), "gpt-3.5-turbo"))

    return response