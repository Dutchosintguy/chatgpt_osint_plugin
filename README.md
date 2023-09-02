# ChatGPT OSINT Plugin

This basic chatgpt plugin leverages MalwareBazaar, VirusTotal, and Hybrid Analysis to provide OSINT on traditional indicators.

## Installation

- Install poetry by running the command: ```pip3 install poetry```
- Install the project by running: ```poetry install``` inside the main directory of the project.
- Create a ```.env``` file in the applications primary directory with the following values:

```
MALWARE_BAZAAR_API_KEY = "YOUR_KEY_HERE"
MALWARE_BAZAAR_API_URL = "https://mb-api.abuse.ch/api/v1/"
VIRUS_TOTAL_API_KEY = "YOUR_KEY_HERE"
VIRUS_TOTAL_API_URL = "https://www.virustotal.com/api/v3/"
HYBRID_ANALYSIS_API_KEY = "YOUR_KEY_HERE"
HYBRID_ANALYSIS_URL = "https://www.hybrid-analysis.com/api/v2/"
```

- Start the project by running: ```poetry run start```
- Access chat.openai.com and select 'alpha', click either 'no plugins enabled' or if you have them enabled, click the icon to present the plugins installed.
- Access the plugin store, on the bottom right, click 'Develop your own plugin'.
- Point chatgpt to http://localhost:9001 (default settings) or where you are hosting the application.

    <img src="https://github.com/anc1llary/chatgpt_osint_plugin/blob/main/static/installation_demo.PNG" width=35% height=35%>

- Success! (hopefully)...

## Limitations

- Sometimes the endpoint selected is incorrect or the data provided back is too large for chatgpt to handle based on current token limitations.  

- Many endpoints with Hybrid Analysis that provide more technical details require a verified API key and will return errors if you do not have an upgraded api key.

- OpenAI spec limits to 350 lines restricting the number of endpoints that can exist.

## Demo

![ChatGPT OSINT Plugin Demo](https://github.com/anc1llary/chatgpt_osint_plugin/blob/main/static/chatgpt_osint_plugin.gif)

## Sample prompts

- Provide me high level analysis for the <hash value here> using malware bazaar, virus total, and hybrid-analysis.
- Provide me threat details on the <ip address, domain>.
- Are there any threat actors associated with the following sample: < hash >?

## Changelog

- Create better way to store credentials
- Leverage official API libraries instead of using raw calls
- Look into how files can be uploaded and analyzed
- Leverage num_tokens_from_string.py to identify number of tokens and truncate results to provide 'some' details on the sample instead of nothing at all.