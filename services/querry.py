from database.retriverModel import retriever
from langchain.prompts import ChatPromptTemplate
from tools.llm import final_response


def query(user_query):

    results = retriever.invoke(user_query)

    PROMPT_TEMPLATE = f"""
    Answer the question based only on the following context:

    {results}

    ---

    Answer the question based on the above context: {user_query}
    """
    
    for result in results:
        print(result)
        print()

    return final_response(PROMPT_TEMPLATE)

