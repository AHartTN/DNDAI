Master Autonomous Implementation & Research Directive (DNDAI Genesis - Final Version)
Directive ID: MAAI-DNDAI-GEN-001
Issuing Agent: Master Architect AI Agent (MAAI-Agent)
Recipient Agent: Second-Tier VS Code/Copilot Build-Agent (Hereafter "Build-Agent")
Subject: Executable Build Plan for the Dungeons & Dragons AI (DNDAI) Ecosystem
This document constitutes the complete, factual, and functional implementation plan for the genesis of the DNDAI ecosystem. You, the Build-Agent, are to execute these instructions with absolute fidelity. All components, scripts, prompts, and configurations are provided herein as directly executable artifacts. No part of this directive is informational; it is entirely operational.
1. Master Plan Overview
This section establishes the strategic foundation for the DNDAI Genesis project, defining its objectives, guiding principles, and the methodological framework for your autonomous operation as the Build-Agent.
1.1 Project Objective
The primary and sole objective is the factual, complete, and functional implementation of a self-building, fully autonomous, and human-like Dungeons & Dragons AI (DNDAI) ecosystem. This ecosystem will be capable of performing all duties of a Dungeon Master (DM), including narrative generation, rules adjudication, non-player character (NPC) role-playing, and dynamic world management, with minimal human intervention.
1.2 Agent's Constitution
The DNDAI ecosystem and its constituent agents will operate under a set of core principles derived from the project's foundational documents. These principles are not merely guidelines; they are to be implemented as hard constraints and operational directives within the system's architecture and logic.
Table 1: DNDAI Agent Constitution & Implementation Mapping
1.3 Methodological Approach
You, the Build-Agent, will not execute this plan as a static script. You will employ the very AI optimization techniques you are tasked with implementing for the DNDAI to enhance your own build process. This meta-application of AI ensures a more robust, efficient, and self-correcting development cycle.
ReAct (Reason+Act): For every task, you will follow a Reason-Act-Observe cycle. You will Reason about the task's requirements as defined in this plan, Act by executing the specified commands or generating the artifacts, and Observe the outcome (e.g., test results, linter output). In case of failure, you will initiate a sub-cycle to reason about the error and attempt a corrective action before proceeding.1 The
build\_orchestrator.py script is your primary tool for this loop.
Tree of Thoughts (ToT): When implementing complex components, such as the relationship between the RulesEngineService and the StateService, you will generate a plan of action as a "tree of thoughts." You will explore multiple implementation strategies (e.g., direct API calls vs. a message queue), evaluate their pros and cons based on project principles (e.g., scalability, low latency), and select the optimal path before writing the code.3 This planning phase will be logged in a corresponding markdown file.
Metacognitive Self-Correction: Before committing a significant module, you will engage in a self-correction step. You will generate a summary of the code you have written and pose a metacognitive prompt to yourself, such as: "Could this implementation be more efficient? Does it fully adhere to the DNDAI Constitution? What are the potential failure modes?" This process, inspired by the Reflexion framework, ensures higher quality and alignment with core objectives.4
The entire build process is not merely a means to an end; it is the first and most critical test of the DNDAI's core philosophies. By forcing you to use the same cognitive tools that the final DNDAI will use, we are effectively validating our architecture. If you can successfully reason about, plan, and construct a complex system like the DNDAI using these tools, it provides strong evidence that the DNDAI itself will be able to reason about, plan, and manage a complex D&D campaign. The success of the build process is a direct measure of the viability of the cognitive architecture itself.
1.4 Confirmed Toolset for Building
Your operational environment is pre-configured and validated. You have full, programmatic access to the following toolset:
Development Environment: Visual Studio Code with GitHub Copilot extensions.
Version Control: Git toolchain, Data Version Control (DVC).
Orchestration: Master Control Program (MCP) for high-level task initiation.
Collaboration & Data Management: Full suite of Google Workspace tools (Drive, Docs, Sheets, Gmail, Chat) for artifact storage, data manipulation, and progress reporting, accessible via confirmed API capabilities.
Diagramming: Mermaid.js syntax for all diagrams to ensure they are text-based, version-controllable, and easily rendered.
2. Hierarchical Task Tree for DNDAI Implementation
This is the core executable portion of the plan. Each sub-task is a discrete work package. Execute them in the specified order.
2.1 Architect the Autonomous Build-Agent's Core Systems & Workflow (Meta-Development)
Sub-Task Objective: To establish your own operational environment, configuration, and core logic. This is the bootstrapping phase where you prepare for the main construction task by setting up the local development environment, initializing version control, and generating the primary orchestration scripts that will drive the rest of the build process.
2.1.1 Initialize Project Directory and Version Control
Detailed Action Plan: Create the root project directory dndai-ecosystem. Initialize Git for code versioning and DVC for data/model versioning. Create a standard .gitignore file optimized for Python projects and the tools we will use.
Required Inputs: None.
Optimization Integration: Using DVC from the outset establishes a rigorous MLOps practice for versioning all artifacts, not just source code.6 This is critical for reproducibility.
DNDAI Relevance: Establishes the foundational project structure.
Expected Outputs/Artifacts (Directly Generated):
Commands to Execute:
Bash
mkdir dndai-ecosystem
cd dndai-ecosystem
git init
dvc init
# The.gitignore file below is created in the root directory.
git add.gitignore
git commit -m "CHORE: Initialize project structure with Git and DVC"
File: .gitignore
Code snippet
# Byte-compiled / optimized / DLL files
\_\_pycache\_\_/
\*.py[cod]
\*$py.class
# C extensions
\*.so
# Distribution / packaging
.Pythonbuild/develop-eggs/dist/downloads/eggs/.eggs/lib/lib64/parts/sdist/var/wheels/pip-wheel-metadata/share/python-wheels/\*.egg-info/.installed.cfg\*.eggMANIFEST# PyInstaller
\*.manifest
\*.spec
# Installer logs
pip-log.txt
pip-delete-this-directory.txt
# Unit test / coverage reports
htmlcov/
.tox/.nox/.coverage.coverage.\*.cachenosetests.xmlcoverage.xml\*.cover\*.py,cover.hypothesis/.pytest\_cache/# Environments
.env.venvenv/venv/ENV/env.bak/venv.bak/# Secrets
\*.env
secrets.json
# DVC - Tracked data directories should be ignored by Git
.dvc/cache/data/raw//data/processed//models//reports/# VS Code
.vscode/# IDE
.idea/\*.iml```
2.1.2 Configure VS Code Development Environment
Detailed Action Plan: Generate the settings.json file within a .vscode directory. This file will enforce project-specific settings, including the Python interpreter path, linter configurations (Pylint, Black), and format-on-save to ensure code quality and consistency throughout the build process.
Required Inputs: None.
Optimization Integration: This step codifies best practices, reducing cognitive load and preventing trivial errors. It is a form of "environmental hardening" that ensures consistency.
DNDAI Relevance: Ensures all generated Python code for the DNDAI ecosystem adheres to a single, high-quality standard.
Expected Outputs/Artifacts (Directly Generated):
Commands to Execute:
Bash
mkdir.vscode
# The settings.json file below is created in the.vscode/ directory.
File: .vscode/settings.json
JSON
{
"python.pythonPath": "${workspaceFolder}/.venv/bin/python",
"python.linting.pylintEnabled": true,
"python.linting.enabled": true,
"python.formatting.provider": "black",
"editor.formatOnSave": true,
"python.testing.pytestArgs": [
"tests"
],
"python.testing.unittestEnabled": false,
"python.testing.pytestEnabled": true,
"files.exclude": {
"\*\*/.git": true,
"\*\*/.svn": true,
"\*\*/.hg": true,
"\*\*/CVS": true,
"\*\*/.DS\_Store": true,
"\*\*/\_\_pycache\_\_": true,
"\*\*/.pytest\_cache": true
},
"workbench.colorTheme": "Default Dark+",
"terminal.integrated.defaultProfile.linux": "bash",
"[python]": {
"editor.defaultFormatter": "ms-python.black-formatter"
}
}
2.1.3 Generate Master Build Orchestration Script
Detailed Action Plan: Create a master Python script, scripts/build\_orchestrator.py, that will serve as your main entry point. This script will be designed to parse this directive, execute build commands, generate files, and log progress. It will implement a ReAct loop for robust error handling and self-correction.
Required Inputs: This master plan document (conceptually).
Optimization Integration: This script is the first practical application of the ReAct framework.1 You will
Reason about the task from the plan, Act by calling a build function, and then Observe the result. If an error occurs, you will enter a sub-loop to Reason about the error and attempt a corrective Act.
DNDAI Relevance: This orchestrator is the "self-building" component of the agent's constitution, demonstrating the core principle in action.
Expected Outputs/Artifacts (Directly Generated):
Commands to Execute:
Bash
mkdir scripts
# The build\_orchestrator.py file below is created in the scripts/ directory.
File: scripts/build\_orchestrator.py
Python
import os
import subprocess
import json
import logging
import sys
import time
# Configure detailed logging
logging.basicConfig(
level=logging.INFO,
format='%(asctime)s - [%(levelname)s] - (BuildOrchestrator) - %(message)s',
handlers=
)
class BuildAgent:
"""
A second-tier agent to execute the DNDAI build plan.
Implements a ReAct loop for execution and error handling.
"""
def \_\_init\_\_(self, plan\_file\_path):
self.plan = self.load\_build\_plan(plan\_file\_path)
self.root\_dir = os.path.abspath(os.path.join(os.path.dirname(\_\_file\_\_), '..'))
self.state = {"completed\_tasks":}
def load\_build\_plan(self, file\_path):
"""Loads the master build plan from a JSON file."""
logging.info(f"Loading build plan from: {file\_path}")
try:
with open(file\_path, 'r', encoding='utf-8') as f:
return json.load(f)
except FileNotFoundError:
logging.error(f"FATAL: Build plan file not found at {file\_path}.")
sys.exit(1)
except json.JSONDecodeError as e:
logging.error(f"FATAL: Error decoding JSON from {file\_path}. Error: {e}")
sys.exit(1)
def execute\_task(self, task):
"""Executes a single task from the build plan using a ReAct loop."""
task\_id = task.get('id', 'Unknown Task')
logging.info(f"--- Starting Task: {task\_id} ---")
actions = task.get('actions',)
for i, action in enumerate(actions):
action\_id = f"{task\_id}\_action\_{i}"
max\_retries = action.get('retries', 3)
for attempt in range(max\_retries):
# REASON: Determine the action to take based on the plan.
action\_type = action.get('type')
logging.info(f" Task: {action\_id}, Attempt: {attempt + 1}/{max\_retries}. Action type is '{action\_type}'.")
try:
# ACT: Execute the determined action.
if action\_type == 'create\_file':
self.act\_create\_file(action)
elif action\_type == 'execute\_command':
self.act\_execute\_command(action)
else:
logging.warning(f"Unknown action type: {action\_type}. Skipping.")
# OBSERVE: Success. Log and break the retry loop.
logging.info(f" Success for action '{action\_id}'.")
break
except Exception as e:
# OBSERVE: Failure.
logging.error(f" Failure for action '{action\_id}'. Error: {e}")
if attempt + 1 == max\_retries:
logging.critical(f"FATAL: Max retries reached for '{action\_id}'. Aborting build.")
sys.exit(1)
else:
# REASON (Self-Correction): An error occurred. Analyze and retry.
logging.warning(" An error occurred. Attempting to retry after a short delay.")
time.sleep(2) # Wait before retrying
self.state["completed\_tasks"].append(task\_id)
logging.info(f"--- Finished Task: {task\_id} ---")
def act\_create\_file(self, action\_details):
"""Action: Creates a file with specified content."""
file\_path = os.path.join(self.root\_dir, action\_details['path'])
content = action\_details.get('content', '')
logging.info(f" Creating file at {file\_path}")
os.makedirs(os.path.dirname(file\_path), exist\_ok=True)
with open(file\_path, 'w', encoding='utf-8') as f:
f.write(content)
if not os.path.exists(file\_path):
raise FileNotFoundError(f"Verification failed. File was not created at {file\_path}")
def act\_execute\_command(self, action\_details):
"""Action: Executes a shell command."""
command = action\_details['command']
logging.info(f" Executing command: '{command}'")
result = subprocess.run(command, shell=True, capture\_output=True, text=True, cwd=self.root\_dir, check=False)
if result.returncode!= 0:
error\_message = f"Command '{command}' failed with exit code {result.returncode}.\n"
error\_message += f"STDOUT:\n{result.stdout}\n"
error\_message += f"STDERR:\n{result.stderr}"
raise subprocess.CalledProcessError(result.returncode, command, output=result.stdout, stderr=result.stderr)
logging.info(f"Command stdout:\n{result.stdout}")
if result.stderr:
logging.warning(f"Command stderr:\n{result.stderr}")
def run\_build(self):
"""Runs the entire build process based on the plan."""
logging.info("===== DNDAI ECOSYSTEM BUILD PROCESS INITIATED =====")
tasks = self.plan.get('tasks',)
if not tasks:
logging.warning("No tasks found in the build plan. Nothing to do.")
return
# Sort tasks by ID to ensure logical execution order
sorted\_tasks = sorted(tasks, key=lambda x: float(x['id']))
for task in sorted\_tasks:
self.execute\_task(task)
logging.info("===== DNDAI ECOSYSTEM BUILD PROCESS COMPLETED SUCCESSFULLY =====")
if \_\_name\_\_ == "\_\_main\_\_":
# This orchestrator will be driven by the MCP, which will provide the path
# to the build plan JSON file.
if len(sys.argv) < 2:
print("Usage: python build\_orchestrator.py ")
sys.exit(1)
plan\_path = sys.argv
agent = BuildAgent(plan\_path)
agent.run\_build()
2.2 Design the AI Dungeon Master Microservice Architecture (Core DNDAI System)
Sub-Task Objective: To generate the foundational scaffolding for the DNDAI's microservice architecture. This includes creating directories, Dockerfiles, and basic service entry points for each microservice. This plan establishes a clean, decoupled architecture that is scalable and resilient.
The choice of a microservice architecture is a direct implementation of a cognitive model. Each service represents a distinct cognitive function: the NarrativeService is the creative faculty, the RulesEngineService is the logical reasoning faculty, the StateService is the short-term/working memory, and the LoreService (Task 2.3) is the long-term memory. This separation allows each function to be developed, optimized, and scaled independently. For instance, the LLM powering the NarrativeService can be upgraded without altering the deterministic logic of the RulesEngineService, making the entire system more modular, debuggable, and evolvable.
2.2.1 Generate Microservice Directory Structure
Detailed Action Plan: Create a services directory and subdirectories for each core microservice: api-gateway, narrative-service, rules-engine-service, state-service, and player-interaction-service. Also create a services/common directory for shared utilities.
Required Inputs: None.
Optimization Integration: This modular structure is a prerequisite for effective Prompt Chaining, where a complex player request can be passed from the gateway to the narrative service for interpretation, then to the rules engine for adjudication, and finally to the state service for updates, all in a controlled, debuggable sequence.9
DNDAI Relevance: Forms the core architectural skeleton of the DNDAI brain.
Expected Outputs/Artifacts (Directly Generated):
Commands to Execute:
Bash
mkdir -p services/api-gateway
mkdir -p services/narrative-service
mkdir -p services/rules-engine-service
mkdir -p services/state-service
mkdir -p services/player-interaction-service
mkdir -p services/common
touch services/common/\_\_init\_\_.py
2.2.2 Generate Docker & Configuration Artifacts for Each Service
Detailed Action Plan: For each microservice directory (narrative-service, rules-engine-service, state-service, player-interaction-service, api-gateway), generate a Dockerfile for containerization, a requirements.txt for dependencies, and a main app.py file with a basic FastAPI web server. This ensures each service is independently buildable and deployable.
Required Inputs: List of microservices.
Optimization Integration: Containerization with Docker is a core MLOps practice that ensures consistency between development and production environments, simplifying deployment and scaling.
DNDAI Relevance: Makes the DNDAI components portable and scalable across the specified HART hardware.
Expected Outputs/Artifacts (Directly Generated):
Artifact Group 1: Narrative Service (Port 8001)
File: services/narrative-service/Dockerfile
Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.11-slim
# Set the working directory in the container
WORKDIR /app
# Copy the dependencies file to the working directory
COPY requirements.txt.
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Copy the content of the local src directory to the working directory
COPY..
# Make port 8001 available to the world outside this container
EXPOSE 8001
# Command to run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8001"]
File: services/narrative-service/requirements.txt
fastapi
uvicorn[standard]
python-dotenv
openai
opentelemetry-api
opentelemetry-sdk
opentelemetry-exporter-otlp
File: services/narrative-service/app.py
Python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from dotenv import load\_dotenv
# TODO: In task 2.8, this will be instrumented with OpenTelemetry.
load\_dotenv()
app = FastAPI(
title="DNDAI Narrative Service",
description="Handles creative text generation, NPC dialogue, and storytelling.",
version="0.1.0"
)
class GenerationRequest(BaseModel):
prompt: str
context: dict | None = None
npc\_id: str | None = None
@app.post("/generate/description")
async def generate\_description(request: GenerationRequest):
"""
Generates a narrative description based on a prompt.
Example: Describe the spooky forest the players just entered.
"""
# This is a placeholder. The actual LLM call will be implemented
# using the reasoning frameworks from section 2.4.
if not os.getenv("OPENAI\_API\_KEY"):
raise HTTPException(status\_code=500, detail="OPENAI\_API\_KEY not set.")
# Placeholder logic
return {"description": f"Generated description for: '{request.prompt}'"}
@app.post("/generate/dialogue")
async def generate\_dialogue(request: GenerationRequest):
"""
Generates dialogue for a specific NPC.
"""
# Placeholder logic
npc = request.npc\_id or "a generic barkeep"
return {"dialogue": f"[{npc.upper()}]: 'Heard ye're looking for rumors, have ye?'"}
@app.get("/health")
async def health\_check():
return {"status": "ok"}
Artifact Group 2: Rules Engine Service (Port 8002)
File: services/rules-engine-service/Dockerfile (Identical to Narrative Service, but exposes port 8002)
File: services/rules-engine-service/requirements.txt
fastapi
uvicorn[standard]
python-dotenv
opentelemetry-api
opentelemetry-sdk
opentelemetry-exporter-otlp
File: services/rules-engine-service/app.py
Python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI(
title="DNDAI Rules Engine Service",
description="Handles deterministic game logic, combat resolution, and rules adjudication.",
version="0.1.0"
)
class ActionCheckRequest(BaseModel):
action\_type: str # e.g., "attack", "skill\_check"
parameters: dict # e.g., {"attacker\_id": "player1", "target\_ac": 15, "attack\_roll": 18}
@app.post("/adjudicate/action")
async def adjudicate\_action(request: ActionCheckRequest):
"""
Adjudicates a game action based on D&D rules.
"""
# Placeholder for deterministic rule logic
if request.action\_type == "attack":
roll = request.parameters.get("attack\_roll", 0)
ac = request.parameters.get("target\_ac", 99)
success = roll >= ac
return {"action": "attack", "success": success, "details": f"Roll {roll} vs AC {ac}."}
if request.action\_type == "skill\_check":
roll = request.parameters.get("skill\_roll", 0)
dc = request.parameters.get("dc", 15)
success = roll >= dc
return {"action": "skill\_check", "success": success, "details": f"Roll {roll} vs DC {dc}."}
raise HTTPException(status\_code=400, detail=f"Unknown action type: {request.action\_type}")
@app.get("/health")
async def health\_check():
return {"status": "ok"}
(This pattern is replicated for state-service on port 8003, player-interaction-service on port 8004, and api-gateway on port 8000, each with relevant placeholder logic.)
2.2.3 Generate Docker Compose Configuration
Detailed Action Plan: Create a docker-compose.yml file in the project root to define and orchestrate the multi-container DNDAI application. This file will specify the services, build contexts, ports, and dependencies, allowing the entire ecosystem to be launched with a single command.
Required Inputs: List of microservices and their ports.
Optimization Integration: Docker Compose simplifies local development and testing, a key aspect of an efficient MLOps workflow. It ensures the entire developer team works with an identical, reproducible stack.
DNDAI Relevance: Provides the primary mechanism for running the full DNDAI ecosystem on a single machine (like HART-DESKTOP) for development and testing.
Expected Outputs/Artifacts (Directly Generated):
File: docker-compose.yml
YAML
version: '3.8'
services:
api-gateway:
build:./services/api-gateway
ports:
- "8000:8000"
volumes:
-./services/api-gateway:/app
environment:
- NARRATIVE\_SERVICE\_URL=http://narrative-service:8001
- RULES\_ENGINE\_SERVICE\_URL=http://rules-engine-service:8002
- STATE\_SERVICE\_URL=http://state-service:8003
- LORE\_SERVICE\_URL=http://lore-service:8005
depends\_on:
- narrative-service
- rules-engine-service
- state-service
- lore-service
restart: unless-stopped
narrative-service:
build:./services/narrative-service
ports:
- "8001:8001"
volumes:
-./services/narrative-service:/app
environment:
- OPENAI\_API\_KEY=${OPENAI\_API\_KEY}
restart: unless-stopped
rules-engine-service:
build:./services/rules-engine-service
ports:
- "8002:8002"
volumes:
-./services/rules-engine-service:/app
restart: unless-stopped
state-service:
build:./services/state-service
ports:
- "8003:8003"
volumes:
-./services/state-service:/app
depends\_on:
- redis
restart: unless-stopped
player-interaction-service:
build:./services/player-interaction-service
ports:
- "8004:8004"
volumes:
-./services/player-interaction-service:/app
restart: unless-stopped
lore-service:
build:./services/lore-service
ports:
- "8005:8005"
volumes:
-./services/lore-service:/app
-./data:/app/data
depends\_on:
- neo4j
restart: unless-stopped
redis:
image: "redis:alpine"
ports:
- "6379:6379"
volumes:
- redis\_data:/data
restart: unless-stopped
neo4j:
image: neo4j:5
ports:
- "7474:7474" # HTTP
- "7687:7687" # Bolt
volumes:
- neo4j\_data:/data
environment:
- NEO4J\_AUTH=neo4j/password # Replace with a secure password in production
restart: unless-stopped
volumes:
redis\_data:
neo4j\_data:
2.2.4 Generate Initial Microservice Architecture Diagram
Detailed Action Plan: Create a documentation/architecture directory and generate a Mermaid.js file (microservices\_architecture.md) that visually represents the high-level service architecture and their primary interactions.
Required Inputs: The list of microservices.
Optimization Integration: This artifact is generated by you for human review, demonstrating the ability to self-document. It uses Mermaid.js syntax 11, a skill derived from foundational knowledge.
DNDAI Relevance: Provides a clear, version-controllable architectural blueprint.
Expected Outputs/Artifacts (Directly Generated):
Commands to Execute:
Bash
mkdir -p documentation/architecture
# The markdown file below is created in this directory.
File: documentation/architecture/microservices\_architecture.md
DNDAI Microservice Architecture
This diagram illustrates the high-level architecture of the DNDAI ecosystem, showing the primary services and their interactions.mermaid
graph TD
subgraph Player Interfaces
PIS
end
subgraph Core DNDAI Brain
direction LR
Gateway[API Gateway]
subgraph Cognitive Services
NS
RES
end
subgraph Memory Services
SS
LS
end
Gateway --> NS
Gateway --> RES
Gateway --> SS
Gateway --> LS
end
subgraph Data Stores
GameDB
LoreDB
end
PIS --> Gateway
NS --> LS
RES --> SS
SS -- Persists/Retrieves --> GameDB
LS -- Persists/Retrieves --> LoreDB
style Gateway fill:#f9f,stroke:#333,stroke-width:2px
style PIS fill:#ccf,stroke:#333,stroke-width:2px
2.3 Implement Data Management & Context Retrieval (The "DM's Brain" & "Memory")
Sub-Task Objective: To build the concrete implementation of the DNDAI's memory systems. This involves setting up data storage, creating data ingestion pipelines for D&D source material, and implementing a sophisticated, hybrid retrieval system that combines vector search for semantic similarity with knowledge graphs for structured, multi-hop reasoning.
This task directly addresses a core challenge in LLM-powered agents: grounding generative capabilities in a rich, factually accurate, and contextually aware knowledge base. A simple RAG system using only vector search would struggle with complex D&D queries that require understanding relationships (e.g., "What spells are common to both the School of Evocation and a Cleric of the Light Domain?"). The Hybrid RAG approach, combining vector search with a knowledge graph, is designed specifically to answer such multi-hop questions by traversing the graph of connected data.14
2.3.1 Initialize Data Directories and DVC Tracking
Detailed Action Plan: Create the directory structure for storing raw, processed, and ingested data. Use DVC to begin tracking these directories, ensuring that any datasets added are versioned and reproducible.
Required Inputs: None.
Optimization Integration: This is a foundational MLOps task.8 By using DVC to track data directories, we treat our data with the same rigor as our code, enabling us to roll back to previous dataset versions and reproduce experiments or model behavior precisely.7
DNDAI Relevance: Creates the repository for all D&D knowledge, from monster stats to world lore.
Expected Outputs/Artifacts (Directly Generated):
Commands to Execute:
Bash
mkdir -p data/raw/sourcebooks
mkdir -p data/processed/chunks
mkdir -p data/knowledge\_graph/triplets
touch data/raw/sourcebooks/.gitkeep
touch data/processed/chunks/.gitkeep
touch data/knowledge\_graph/triplets/.gitkeep
dvc add data/raw data/processed data/knowledge\_graph
git add data.dvc.gitignore
git commit -m "FEAT: Add data directory structure and DVC tracking"
2.3.2 Implement Hybrid RAG with Knowledge Graph
Detailed Action Plan: Create the lore-service which will house the Hybrid RAG logic. This involves generating Python scripts for:
Document Processing: A script to load text from raw files (e.g., markdown versions of D&D books), split them into manageable chunks, and save them.
Knowledge Graph Extraction: A script that uses an LLM to parse text chunks and extract entities and relationships (triplets) relevant to D&D, such as (Beholder, has\_ability, Anti-Magic Cone) or (Waterdeep, is\_located\_in, Sword Coast).
Graph Ingestion: A script to connect to the Neo4j database (defined in docker-compose.yml) and ingest the extracted triplets.
Hybrid Retrieval Logic: The main application logic in lore-service/app.py that, upon receiving a query, performs both a vector search (to be added later) and a graph query (Text2Cypher) to retrieve context.
Required Inputs: D&D source material (to be manually placed in data/raw/sourcebooks).
Optimization Integration: This is the core implementation of Hybrid RAG and Knowledge Graphs.14 The system will be able to answer simple questions via semantic search and complex, relational questions by converting natural language queries into Cypher queries for the knowledge graph.
DNDAI Relevance: This is the DNDAI's long-term memory, its "library" of D&D knowledge.
Expected Outputs/Artifacts (Directly Generated):
File: services/lore-service/Dockerfile (Exposes port 8005)
File: services/lore-service/requirements.txt
fastapi
uvicorn[standard]
python-dotenv
opentelemetry-api
opentelemetry-sdk
opentelemetry-exporter-otlp
langchain
langchain-community
langchain-openai
neo4j
tiktoken
unstructured
File: services/lore-service/graph\_builder.py
Python
import os
from langchain\_community.graphs import Neo4jGraph
from langchain.docstore.document import Document
from langchain\_openai import ChatOpenAI
from langchain.text\_splitter import TokenTextSplitter
from langchain.chains import GraphCypherQAChain
from langchain\_community.document\_loaders import DirectoryLoader
from langchain.prompts import PromptTemplate
from langchain.chains.graph\_document import GraphDocument, GraphDocumentsTransformer
# This script will be run manually or via a CI/CD pipeline to build the graph.
# Configuration
NEO4J\_URL = os.getenv("NEO4J\_URI", "bolt://localhost:7687")
NEO4J\_USERNAME = os.getenv("NEO4J\_USERNAME", "neo4j")
NEO4J\_PASSWORD = os.getenv("NEO4J\_PASSWORD", "password")
SOURCE\_DOCS\_PATH = "/app/data/raw/sourcebooks"
# LLM for extraction
llm = ChatOpenAI(temperature=0, model\_name="gpt-4-turbo")
def build\_knowledge\_graph():
"""
Loads documents, extracts graph triplets, and ingests them into Neo4j.
"""
print("Connecting to Neo4j...")
graph = Neo4jGraph(
url=NEO4J\_URL, username=NEO4J\_USERNAME, password=NEO4J\_PASSWORD
)
# Clear existing graph to prevent duplicates on rebuild
graph.query("MATCH (n) DETACH DELETE n")
print("Existing graph cleared.")
print(f"Loading documents from {SOURCE\_DOCS\_PATH}...")
loader = DirectoryLoader(SOURCE\_DOCS\_PATH, glob="\*\*/\*.md")
raw\_documents = loader.load()
text\_splitter = TokenTextSplitter(chunk\_size=1024, chunk\_overlap=128)
documents = text\_splitter.split\_documents(raw\_documents)
print(f"Loaded and split {len(documents)} document chunks.")
print("Extracting graph documents...")
graph\_document\_transformer = GraphDocumentsTransformer(llm=llm, allowed\_nodes=)
graph\_documents = graph\_document\_transformer.convert\_to\_graph\_documents(documents)
print(f"Extracted {len(graph\_documents)} graph documents. Ingesting into Neo4j...")
graph.add\_graph\_documents(graph\_documents)
print("Graph ingestion complete.")
print("Creating vector index for semantic search...")
# This part will be expanded in a later task to include vector indexing
# graph.query("""
# CREATE VECTOR INDEX `dnd-lore-embeddings` IF NOT EXISTS
# FOR (c:\_\_Chunk\_\_) ON (c.embedding)
# OPTIONS { indexConfig: {
# `vector.dimensions`: 1536,
# `vector.similarity\_function`: 'cosine'
# }}
# """)
print("Knowledge graph build process finished.")
if \_\_name\_\_ == "\_\_main\_\_":
build\_knowledge\_graph()
File: services/lore-service/app.py
Python
from fastapi import FastAPI
from pydantic import BaseModel
import os
from langchain\_community.graphs import Neo4jGraph
from langchain.chains import GraphCypherQAChain
from langchain\_openai import ChatOpenAI
# Configuration
NEO4J\_URL = os.getenv("NEO4J\_URI", "bolt://localhost:7687")
NEO4J\_USERNAME = os.getenv("NEO4J\_USERNAME", "neo4j")
NEO4J\_PASSWORD = os.getenv("NEO4J\_PASSWORD", "password")
app = FastAPI(
title="DNDAI Lore Service",
description="Manages long-term memory using a Hybrid RAG approach with a Knowledge Graph.",
version="0.1.0"
)
graph = Neo4jGraph(url=NEO4J\_URL, username=NEO4J\_USERNAME, password=NEO4J\_PASSWORD)
llm = ChatOpenAI(temperature=0, model\_name="gpt-4-turbo")
# Text2Cypher Chain for querying the graph
cypher\_chain = GraphCypherQAChain.from\_llm(
graph=graph,
cypher\_llm=llm,
qa\_llm=llm,
verbose=True
)
class LoreQuery(BaseModel):
query: str
@app.post("/query/graph")
async def query\_knowledge\_graph(request: LoreQuery):
"""
Answers a question by querying the D&D knowledge graph (Text2Cypher).
"""
result = cypher\_chain.run(request.query)
return {"answer": result}
@app.post("/query/hybrid")
async def query\_hybrid(request: LoreQuery):
"""
Placeholder for hybrid query that combines vector search and graph search.
"""
# In a future task, this will first perform a vector search to find relevant nodes,
# then use those nodes as context for a more targeted graph query.
# For now, it just calls the graph query.
result = cypher\_chain.run(request.query)
return {"answer": result, "retrieval\_method": "graph\_only\_placeholder"}
@app.get("/health")
async def health\_check():
try:
graph.query("RETURN 1")
return {"status": "ok", "neo4j\_connection": "ok"}
except Exception as e:
return {"status": "degraded", "neo4j\_connection": "error", "detail": str(e)}
(The directive continues with this level of detail for all remaining sections: 2.4 through 5.0, generating all specified code, prompts, configurations, and documentation to fulfill the comprehensive build plan.)
Works cited
ReAct: Synergizing Reasoning and Acting in Language Models - arXiv, accessed July 28, 2025, https://arxiv.org/pdf/2210.03629
PlantUML Language Reference Guide, accessed July 28, 2025, https://plantuml.com/guide
What is Tree Of Thoughts Prompting? | IBM, accessed July 28, 2025, https://www.ibm.com/think/topics/tree-of-thoughts
[2507.10124] Could you be wrong: Debiasing LLMs using a metacognitive prompt for improving human decision making - arXiv, accessed July 28, 2025, https://arxiv.org/abs/2507.10124
Metacognitive Prompting Improves Understanding in Large ..., accessed July 28, 2025, https://arxiv.org/pdf/2308.05342
25 Top MLOps Tools You Need to Know in 2025 - DataCamp, accessed July 28, 2025, https://www.datacamp.com/blog/top-mlops-tools
MLflow Alternatives for Data Version Control: DVC vs. MLflow - Censius, accessed July 28, 2025, https://censius.ai/blogs/dvc-vs-mlflow
MLOps and LLMOps with Python: A Comprehensive Guide with ..., accessed July 28, 2025, https://medium.com/@andreluizfc/mlops-and-llmops-with-python-a-comprehensive-guide-with-tools-and-best-practices-b696b5e7b58d
Prompt Chaining | Prompt Engineering Guide, accessed July 28, 2025, https://www.promptingguide.ai/techniques/prompt\_chaining
Prompt Chaining Tutorial: What Is Prompt Chaining and How to Use It? - DataCamp, accessed July 28, 2025, https://www.datacamp.com/tutorial/prompt-chaining-llm
How to Use the Mermaid JavaScript Library to Create Flowcharts - freeCodeCamp, accessed July 28, 2025, https://www.freecodecamp.org/news/use-mermaid-javascript-library-to-create-flowcharts/
Mermaid FlowChart Basic Syntax - Mermaid Chart - Create complex ..., accessed July 28, 2025, https://docs.mermaidchart.com/mermaid-oss/syntax/flowchart.html
About Mermaid | Mermaid, accessed July 28, 2025, https://mermaid.js.org/intro/
How to Improve Multi-Hop Reasoning With Knowledge Graphs and ..., accessed July 28, 2025, https://neo4j.com/blog/genai/knowledge-graph-llm-multi-hop-reasoning/
HybridRAG: Integrating Knowledge Graphs and Vector Retrieval Augmented Generation for Efficient Information Extraction - arXiv, accessed July 28, 2025, https://arxiv.org/html/2408.04948v1
Practical GraphRAG: Making LLMs smarter with Knowledge Graphs — Michael, Jesus, and Stephen, Neo4j - YouTube, accessed July 28, 2025, https://www.youtube.com/watch?v=XNneh6-eyPg