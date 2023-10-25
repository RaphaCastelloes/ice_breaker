import json
import os
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from agents import linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile

if __name__ == '__main__':
    print('Hello LangChain!')

summary_template = '''
given the information {information} about a person from I want to create:
1. a short summary
2. two interesting facts about them
'''

linkedin_profile_url = linkedin_lookup_agent.lookup(name="Eden Marco Udemy")

summary_prompt_template = PromptTemplate(
    input_variables=["information"], template=summary_template)

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo") # type: ignore the model_name they exists in openai.py

chain = LLMChain(llm=llm, prompt=summary_prompt_template)

linkedin_data = scrape_linkedin_profile(
    linkedin_profile_url=linkedin_profile_url)

result = chain.run(information=linkedin_data)

print(result)
input()