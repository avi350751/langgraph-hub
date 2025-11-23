from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

class BlogState(TypedDict):
    title:str
    outline:str
    content:str

def get_blog(model):

    def create_outline(state:BlogState) -> BlogState:

        title = state['title']
        prompt = f"Create a detailed outline for a blog post about: {title}"
        outline = model.invoke(prompt).content
        state['outline'] = outline
        return state

    def create_blog(state:BlogState) -> BlogState:

        title = state['title']
        outline = state['outline']
        prompt = f"Write a comprehensive blog based on the title : {title} using the following outline: {outline}"
        content = model.invoke(prompt).content
        state['content'] = content
        return state

    graph = StateGraph(BlogState)

    #nodes
    graph.add_node('create_outline', create_outline)
    graph.add_node('create_blog', create_blog)

    #edges
    graph.add_edge(START, 'create_outline')
    graph.add_edge('create_outline', 'create_blog')
    graph.add_edge('create_blog', END)

    workflow = graph.compile()
    return workflow

#execute workflow
def run_workflow(title: str):

    app = get_blog(model)
    result = app.invoke({"title": title})
    return result

