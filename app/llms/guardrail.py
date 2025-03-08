from app.prompts.prompts import guardrail_prompt
from app.llms.llms import gemma


def guardrail(query: str) -> bool:
    prompt = guardrail_prompt.format(user_query=query)
    response = gemma.invoke(prompt)
    if response.content.strip() == "REJECT":
        return False
    return True