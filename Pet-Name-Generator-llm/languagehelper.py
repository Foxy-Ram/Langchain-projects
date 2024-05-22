from langchain.llms.google_palm import GooglePalm
from secretkey import GOOGLE_PALM_API_KEY
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

api_key = GOOGLE_PALM_API_KEY #Importing api-key

#Initializig LLM
llm = GooglePalm(google_api_key=GOOGLE_PALM_API_KEY, temprature=0.3)

def get_petNames(pet_name:str, pet_color:str, llm=llm)-> dict:
    #Creating Prompt using prompt template
    template = " Provide list of 5 names only for my pet {pet_name} & {pet_color} in color."
    prompt = PromptTemplate(
        input_variables = ["pet_name","pet_color"],
        template = template
    )

    #Creating chain
    name_chain = LLMChain(llm = llm, prompt = prompt, output_key = "names")
    response = name_chain({"pet_name" : pet_name, "pet_color" : pet_color})
    
    return response

if __name__ == "__main__":
    response = get_petNames(pet_name="dog", pet_color="black").get("names")
    print(response)