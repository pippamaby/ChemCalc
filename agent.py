from langchain_ollama import ChatOllama
from tools import reynolds_number, heat_duty, pressure_drop


llm = ChatOllama(model="qwen3")

tools = [reynolds_number, heat_duty, pressure_drop]

llm_with_tools = llm.bind_tools(tools)


def ask_chemcalc(question):
    response = llm_with_tools.invoke(question)

    if response.tool_calls:
        tool_call = response.tool_calls[0]

        tool_name = tool_call["name"]
        tool_args = tool_call["args"]

        for tool in tools:
            if tool.name == tool_name:
                return tool.invoke(tool_args)

    return response.content

def ask_chemcalc(question):
    response = llm_with_tools.invoke(question)

    if response.tool_calls:
        tool_call = response.tool_calls[0]

        tool_name = tool_call["name"]
        tool_args = tool_call["args"]

        for tool in tools:
            if tool.name == tool_name:
                result = tool.invoke(tool_args)
                return result

    return response.content