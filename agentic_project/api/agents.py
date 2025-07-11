# api/agents.py - The Final, Correct, and Complete Version

import os
import uuid
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from crewai_tools import WebsiteSearchTool
from langchain_openai import ChatOpenAI, OpenAIEmbeddings # Correct, modern imports
from qdrant_client import QdrantClient, models

load_dotenv()

# --- LLM and Embedding Model SETUP ---
openai_llm = ChatOpenAI(
    model="gpt-4",
    openai_api_key=os.getenv("OPENAI_API_KEY")
)
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small", # A modern and cost-effective embedding model
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# --- QDRANT SETUP (Cloud Persistent Storage) ---
client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
)
collection_name = "company_research_v2" # Use a new collection name to ensure no old data conflicts
try:
    client.get_collection(collection_name=collection_name)
except Exception:
    # Vector size for text-embedding-3-small is 1536
    client.create_collection(
        collection_name=collection_name,
        vectors_config=models.VectorParams(size=1536, distance=models.Distance.COSINE)
    )

# --- AGENTS SETUP ---
# The Agent constructor is now written out completely and correctly.
researcher = Agent(
    role='Senior Market Researcher',
    goal='Find and analyze information on the target company\'s website to understand its business and potential needs.',
    backstory='You are an expert market researcher, skilled in using search tools to find and synthesize information from specific websites.',
    verbose=True,
    allow_delegation=False,
    # The tool is not needed here if we use it directly in the task for modern versions
    # tools=[WebsiteSearchTool()], 
    llm=openai_llm
)

copywriter = Agent(
    role='Expert Tech Copywriter',
    goal='Write compelling, personalized cold emails that get replies.',
    backstory='You craft persuasive emails based on thorough research provided to you.',
    verbose=True,
    allow_delegation=False,
    llm=openai_llm
)

# --- CREW TASK DEFINITION ---
def create_outreach_crew(company_url: str, product_description: str) -> str:
    query_text = f"{company_url} | {product_description}"
    query_vector = embedding_model.embed_query(query_text)

    search_result = client.search(
        collection_name=collection_name,
        query_vector=query_vector,
        limit=1,
        score_threshold=0.98
    )

    if search_result:
        print("🎉 Found cached result in Qdrant!")
        return search_result[0].payload["email"]

    print("🕵️ No cached result found. Kicking off the AI crew...")
    research_task = Task(
        description=f"Analyze the content of the website: {company_url}.",
        expected_output="A 3-4 sentence summary of the company's mission, products, and key challenges.",
        agent=researcher,
        tools=[WebsiteSearchTool(website_url=company_url)] # Pass the tool directly to the task
    )

    copywriting_task = Task(
        description=f"Using the research report, write a personalized, 2-paragraph cold email. Introduce our product: '{product_description}', and connect it to a challenge or goal identified in the research.",
        expected_output="A complete, ready-to-send email with a compelling subject line.",
        agent=copywriter,
        context=[research_task]
    )

    crew = Crew(
        agents=[researcher, copywriter],
        tasks=[research_task, copywriting_task],
        process=Process.sequential
    )
    result_obj = crew.kickoff()
    final_email = str(result_obj)

    print("💾 Storing new result in Qdrant...")
    client.upsert(
        collection_name=collection_name,
        points=[
            models.PointStruct(
                id=str(uuid.uuid4()),
                vector=query_vector,
                payload={"email": final_email}
            )
        ]
    )
    return final_email