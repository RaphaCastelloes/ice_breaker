import os

import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    # '''Scrape linkedin profile and return a dict of profile data'''
    # api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    # header_dic = {"Authorization": f"Bearer {os.environ['PROXYCURL_API_KEY']}"}
    # response = requests.get(api_endpoint, headers=header_dic, params={
    #                         "url": linkedin_profile_url})

    # response_json = response.json()
    # # clean response_json from json keys with empty values
    # response_json = {k: v for k, v in response_json.items() if v not in [
    #     None, "", "", []] and k not in ["people_also_viewed", "certifications"]}
    # if response_json.get("groups"):
    #     for group in response_json["groups"]:
    #         group.pop("profile_pic_url")

    # # save response_json in a file response.json
    # with open("response.json", "w") as f:
    #     f.write(str(response_json))

    # open response.json
    with open("response.json", "r") as f:
        response_json = f.read()
    
    # convert response_json in json
    response_json = eval(response_json)
    
    return response_json
