from fastapi import APIRouter
from app.services.hybrid_analysis import search_hash as sh
from app.services.hybrid_analysis import analysis_overview as ao
from app.services.hybrid_analysis import memory_hex_dump as mh
from app.services.hybrid_analysis import memory_strings_dump as msd
from app.services.hybrid_analysis import report_summary as rs

router = APIRouter()

@router.post("/search-hash", description="Query hash value against Hybrid Analysis.")

async def search_hash(hash_value: str) -> dict:

    """
    Query a given hash value against the Hybrid Analysis database.

    Parameters:
    hash_value (str): The hash value to query. Should be a valid SHA-256, SHA-1, or MD5 hash.

    Returns:
    dict: The response from the Hybrid Analysis database, typically containing information about
          whether the hash is associated with any known malware.

    Raises:
    HTTPException: If the query to Hybrid Analysis fails for any reason.

    """

    response =  sh.search_hash(hash_value)  
    return response

@router.post("/analysis-overview", description="Get analysis report of a SHA256 hash against Hybrid Analysis.")

async def analysis_overview(sha256: str) -> dict:
 
    """
    Retrieve the analysis overview for a given SHA256 hash from the Hybrid Analysis database.

    Parameters:
    sha256 (str): The SHA256 hash to query.

    Returns:
    dict: The analysis overview from Hybrid Analysis.

    Raises:
    HTTPException: If the query to Hybrid Analysis fails for any reason.

    """
    response =  ao.analysis_overview(sha256) 
    return response

#@router.post("/memory-hex-dump", description="Get analysis details with a hex dump of a SHA256 file from Hybrid Analysis.")

#async def memory_hex_dump(sha256: str) -> dict:

    """
    Retrieve the hex dump of the memory for a given SHA256 file from the Hybrid Analysis database.

    Parameters:
    sha256 (str): The SHA256 hash to query.

    Returns:
    dict: The hex dump of the memory from Hybrid Analysis.

    Raises:
    HTTPException: If the query to Hybrid Analysis fails for any reason.

    """

#   response =  mh.memory_hex_dump(sha256) 
#   return response

#@router.post("/memory-strings-dump", description="Get strings extracted from memory a SHA256 file from Hybrid Analysis.")

#async def memory_strings_dump(sha256: str)-> dict:

    """
    Retrieve the strings extracted from the memory of a given SHA256 file from the Hybrid Analysis database.

    Parameters:
    sha256 (str): The SHA256 hash to query.

    Returns:
    dict: The strings extracted from the memory from Hybrid Analysis.

    Raises:
    HTTPException: If the query to Hybrid Analysis fails for any reason.

    """

#    response =  msd.memory_strings_dump(sha256) 
#    return response

@router.post("/report-summary", description="Get the report summary for a SHA256 file from Hybrid Analysis.")

async def report_summary(sha256: str) -> dict:
    
    """
    Retrieve the report summary for a given SHA256 file from the Hybrid Analysis database.

    Parameters:
    sha256 (str): The SHA256 hash to query.

    Returns:
    dict: The report summary from Hybrid Analysis.

    Raises:
    HTTPException: If the query to Hybrid Analysis fails for any reason.

    """
    
    response =  rs.report_summary(sha256)
    return response