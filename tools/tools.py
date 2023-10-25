import os
from langchain.serpapi import SerpAPIWrapper

def get_profile_url(text:str) -> str:
    '''Searchs for Linkedin of Profile'''
    search = SerpAPIWrapper(serpapi_api_key=os.environ["SERP_API_KEY"]) # type: ignore
    return search.run(text)