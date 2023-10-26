from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from agents import linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile
from models.person_intel import PersonIntel, person_intel_parser


def ice_breaker(name: str) -> PersonIntel:
    template = '''
given a the Linkedin information {linkedin_information} about a person from I want you to create:
1. a short summary
2. two interesting facts about them
3. A topic that may interest them
4. An ice breaker to start a conversation with them
\n
{format_instructions}
'''
    linkedin_profile_url = linkedin_lookup_agent.lookup(name=name)

    prompt = PromptTemplate(
        input_variables=["information"],
        template=template,
        partial_variables={
            "format_instructions": person_intel_parser.get_format_instructions()}
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")  # type: ignore

    chain = LLMChain(llm=llm, prompt=prompt)

    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_profile_url)

    result = chain.run(linkedin_information=linkedin_data)
    
    return person_intel_parser.parse(result)


if __name__ == '__main__':
    print('Hello LangChain!')
    result = ice_breaker("Harrison Chase")
    print(result)
    input()
