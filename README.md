Absolutely. Here is the full Neon Core Agent V1 plan in English, ready to give directly to your other coding agent.
Neon Core Agent V1 — Full Development Plan
1. Project Goal
Build Neon Core, a persistent digital agent that can:
Chat with the user
Use tools
Browse the web
Search and research
Run shell commands
Execute Python code
Use Node.js tools
Use MCP servers
Connect to APIs
Manage files
Work with GitHub
Run long-running processes
Observe tool results in real time
Verify whether a task actually succeeded
Recover from failures
Maintain persistent memory
Organize/clean memory automatically
Sleep and perform memory maintenance
Resume interrupted tasks
Switch between local and cloud LLMs
Eventually control applications/games such as Minecraft
The important principle is:
Neon is an agent, not merely a chatbot.
2. Core Architecture
                    USER
                      │
                      ▼
                 WEB UI / API
                      │
                      ▼
               NEON CORE AGENT
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
     MEMORY SYSTEM            MODEL ROUTER
                                  │
                         ┌────────┴────────┐
                         ▼                 ▼
                    LOCAL LLM        CLOUD LLM
                    llama.cpp       Gemini/etc.
                         │
                         └────────┬────────┘
                                  ▼
                           AGENT PLANNER
                                  │
                                  ▼
                           TOOL MANAGER
                                  │
              ┌───────────┬───────┼──────────┐
              ▼           ▼       ▼          ▼
           Python       Shell    Node.js     MCP
            Tools       Tools    Runtime    Servers
              │           │       │          │
              └───────────┴───────┴──────────┘
                                  │
                                  ▼
                         PROCESS MANAGER
                                  │
                                  ▼
                         OBSERVE / VERIFY
                                  │
                       ┌──────────┴──────────┐
                       ▼                     ▼
                    SUCCESS               FAILURE
                       │                     │
                       ▼                     ▼
                    FINISH              RECOVER/RETRY
3. Python vs Node.js
Use:
Python = Main Agent
Python controls:
Agent loop
Planning
Model routing
Memory
RAG
Skills
Tool registry
MCP
Task management
Process management
Web API
Web UI backend
Recovery
Logging
Node.js = Tool Runtime
Node.js is already available and should be used when a tool requires Node.
For example:
User:
"Join my Minecraft server."

Python Agent:
→ understands task
→ determines Minecraft requires Node.js
→ starts Node runtime
→ installs/loads Mineflayer if required
→ launches persistent Minecraft process
→ observes connection
→ receives server response
→ continues controlling bot
Do not build a second agent in Node.js.
4. Repository Structure
agent-neon-core/
│
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
├── pyproject.toml
├── requirements.txt
│
├── config/
│   └── config.yaml
│
├── neon/
│   ├── __init__.py
│   │
│   ├── agent/
│   │   ├── core.py
│   │   ├── planner.py
│   │   ├── executor.py
│   │   ├── observer.py
│   │   ├── verifier.py
│   │   └── recovery.py
│   │
│   ├── models/
│   │   ├── router.py
│   │   ├── local.py
│   │   └── cloud.py
│   │
│   ├── memory/
│   │   ├── manager.py
│   │   ├── short_term.py
│   │   ├── long_term.py
│   │   ├── rag.py
│   │   ├── cleanup.py
│   │   └── sleep.py
│   │
│   ├── tools/
│   │   ├── registry.py
│   │   ├── shell.py
│   │   ├── filesystem.py
│   │   └── permissions.py
│   │
│   ├── runtime/
│   │   ├── process_manager.py
│   │   ├── node_runtime.py
│   │   └── health.py
│   │
│   ├── integrations/
│   │   ├── mcp.py
│   │   ├── github.py
│   │   ├── browser.py
│   │   └── apis.py
│   │
│   ├── tasks/
│   │   ├── manager.py
│   │   ├── state.py
│   │   └── checkpoint.py
│   │
│   └── api/
│       ├── server.py
│       └── routes.py
│
├── node_runtime/
│   ├── package.json
│   ├── bridge.js
│   └── skills/
│
├── web/
│   ├── index.html
│   ├── app.js
│   └── style.css
│
├── data/
│   ├── memory/
│   ├── tasks/
│   ├── checkpoints/
│   └── logs/
│
└── tests/
5. Phase 1 — Basic Agent
First build only the core.
Implement:
User message
     ↓
Agent
     ↓
LLM
     ↓
Response
Then add:
User
 ↓
Agent
 ↓
LLM
 ↓
Tool selection
 ↓
Tool execution
 ↓
Tool result
 ↓
LLM
 ↓
Final response
The agent must support multiple tool calls in one task.
6. The Most Important Part: Agent Loop
Do NOT make this:
command
→ finish
→ forget
Instead:
Understand task
      ↓
Create plan
      ↓
Execute action
      ↓
Observe result
      ↓
Verify result
      ↓
Decide next action
      ↓
Execute next action
      ↓
Repeat
      ↓
Task completed
Example:
User:
"Join my Minecraft server and play with me."

Agent:

1. Check required Minecraft runtime
2. Check Node.js
3. Check Mineflayer
4. Install if missing
5. Create bot script
6. Start persistent process
7. Connect to server
8. Observe server response
9. Verify bot joined
10. Keep process alive
11. Receive game events
12. Act according to user commands
It must not stop after step 6.
7. Persistent Process Manager
This is extremely important.
Create:
process_manager.py
It should support:
start()
stop()
restart()
status()
send_input()
read_output()
health_check()
checkpoint()
resume()
Processes should have IDs:
process_id
name
command
status
pid
started_at
last_output
health
checkpoint
Example:
minecraft-bot
status: running
PID: 1234
health: healthy
The agent can continue interacting with the same process instead of launching a new terminal every time.
8. Tool System
Create a dynamic tool registry.
Example:
ToolRegistry
 ├── shell
 ├── filesystem
 ├── python
 ├── node
 ├── browser
 ├── github
 ├── MCP
 └── API
Tools should be loaded on demand.
Don't load every tool into memory at startup.
9. Node.js Runtime
Python should be able to do:
Python Agent
     ↓
Node Runtime
     ↓
Node Package
     ↓
Long-running process
The Node runtime should support:
install_package()
run_script()
start_process()
stop_process()
send_command()
read_output()
get_status()
Example:
npm install mineflayer
Then:
node minecraft_bot.js
The process remains alive.
10. Model System
Use a model abstraction.
ModelRouter
     │
     ├── LocalModel
     │      └── llama.cpp
     │
     └── CloudModel
            ├── Gemini
            ├── OpenAI-compatible APIs
            └── Other providers
The rest of the agent should not care which model is being used.
Example:
response = model.generate(messages)
instead of hardcoding Gemini everywhere.
11. Local Model
Initial hardware target:
RAM:     4 GB
CPU:     2 cores
Storage: 20 GB
Use llama.cpp.
The local model should handle:
Simple conversation
Simple decisions
Tool selection
Basic commands
Small tasks
Fast responses
Don't expect a tiny model to perform complex reasoning perfectly.
12. Cloud Fallback
If the local model struggles:
User Request
     ↓
Local Model
     ↓
Can handle?
 ┌───┴───┐
YES      NO
 │        │
 ▼        ▼
Answer   Cloud Model
Also allow explicit routing:
fast → local
normal → local/cloud
complex → cloud
coding → specialized model
The provider API keys should be stored in environment variables, never hardcoded.
13. Memory System
Use multiple memory layers.
Short-Term Memory
Current task:
current conversation
current plan
current tool results
current process state
Long-Term Memory
Things such as:
User preferences
User name
Important facts
Recurring tasks
Projects
Useful decisions
RAG
Store searchable knowledge separately.
Query
 ↓
Retriever
 ↓
Relevant memories
 ↓
Agent context
14. Memory Rules
Very important:
Do NOT save everything.
Save:
Important user facts
Preferences
Long-term goals
Useful project information
Important decisions
Recurring instructions
Don't permanently save:
Every tool output
Every shell command
Temporary errors
Temporary conversation details
Duplicate information
15. Automatic Memory Cleanup
Implement:
Memory Manager
     ↓
Score memories
     ↓
Important?
 ┌───┴───┐
YES      NO
 │        │
KEEP    Review
          ↓
       Delete/Merge
Memory metadata:
created_at
updated_at
importance
confidence
last_used
source
type
Never automatically delete highly important memories just because they are old.
16. Sleep Mode
The agent gets a sleep state:
AWAKE
  ↓
SLEEPING
  ↓
MEMORY CONSOLIDATION
  ↓
CLEANUP
  ↓
CHECKPOINT
  ↓
READY
During sleep:
Organize memories
Merge duplicates
Remove useless temporary memories
Update indexes
Check task state
Clean logs
Verify storage
Create backups/checkpoints
17. Safe Sleep Interruption
Never modify important files directly.
Use:
Original
   ↓
Temporary copy
   ↓
Modify
   ↓
Validate
   ↓
Commit
If interrupted:
checkpoint exists
      ↓
resume later
The UI should show:
😴 Neon is sleeping

Managing memory...
Optimizing storage...

[Interrupt Sleep]
If interrupted, Neon should safely stop its current maintenance operation.
18. MCP System
Build an MCP manager.
It should support:
add server
remove server
enable
disable
start
stop
list tools
execute tool
health check
Example integrations:
GitHub MCP
Filesystem MCP
Browser MCP
Search MCP
Custom MCP
Tools should be discoverable dynamically.
19. Browser
Add a lightweight browser automation layer.
Capabilities:
Open page
Search web
Read page
Click
Type
Scroll
Extract information
Take screenshot
The agent should use browser automation for research instead of trying to perform everything through raw HTTP.
20. GitHub Integration
GitHub should eventually support:
list repositories
read files
search code
create files
update files
create branches
commits
issues
pull requests
Keep GitHub authentication separate from the core agent.
21. Task Manager
Every meaningful task gets:
task_id
user_request
status
plan
current_step
created_at
updated_at
checkpoint
processes
result
States:
PENDING
PLANNING
RUNNING
WAITING
VERIFYING
FAILED
PAUSED
COMPLETED
CANCELLED
22. Recovery System
If something fails:
Failure
 ↓
Understand error
 ↓
Retry?
 ├── YES → retry
 └── NO
       ↓
Alternative method
       ↓
Verify
       ↓
Continue
For example:
npm install failed
        ↓
Check Node
        ↓
Check npm
        ↓
Check network
        ↓
Retry
        ↓
Alternative installation
        ↓
Verify package
The agent should not simply say:
"Installation failed."
It should attempt recovery when safe.
23. Web UI
V1 UI should be simple.
Main screen
┌──────────────────────────────────────────┐
│ Neon Core                         ● Online│
├──────────────┬───────────────────────────┤
│ Chats        │                           │
│ Tasks        │       Chat Area           │
│ Memory       │                           │
│ Tools        │                           │
│ Models       │                           │
│ Processes    │                           │
│ Connections  │                           │
│ Settings     │                           │
└──────────────┴───────────────────────────┘
24. Sidebar
V1:
New Chat

Chats
Tasks
Memory
Tools
Processes
Models
Connections

Sleep
Settings
25. Chat UI
Make it somewhat ChatGPT-like.
Support:
New chat
Chat history
Streaming responses
Tool activity
Task progress
Stop generation
Continue task
Tool execution can appear as:
🔧 Running Node.js...
✓ Node.js available

🔧 Installing Mineflayer...
✓ Installed

🤖 Connecting to server...
✓ Connected

🎮 Minecraft bot is online
26. Task View
Example:
Task: Join Minecraft server

Status: RUNNING

✓ Node.js detected
✓ Mineflayer installed
✓ Bot script created
✓ Process started
✓ Connected to server

Current:
Waiting for game event...

Process:
minecraft-bot
PID: 1932

[Pause] [Stop]
27. Process Dashboard
Show:
Process
Status
CPU
RAM
PID
Uptime
Health
Example:
Minecraft Bot
● Running
RAM: 82 MB
CPU: 2%
PID: 1932
Uptime: 18m
28. Memory UI
Show categories:
Important
Preferences
Projects
Tasks
Facts
Temporary
Allow:
Search
Edit
Delete
Merge
Protect
Protected memories should never be automatically deleted.
29. Security
Because the agent can execute commands, this is critical.
Implement:
Tool permissions
Command restrictions
Environment isolation
Secrets protection
Path restrictions
Process limits
Resource limits
Never expose API keys to the LLM unnecessarily.
30. Resource Management
Target:
4 GB RAM
2 CPU
20 GB storage
Therefore:
Always running
Python Agent
Database
Lightweight API
Lightweight UI
llama.cpp
On demand
Browser
Node tools
MCP servers
Minecraft
Heavy models
Other applications
This keeps the server lightweight.
31. First Real Test
Do not start with Minecraft.
First prove:
User:
"Create a file called test.txt containing Hello Neon."
Agent:
Plan
 ↓
Filesystem tool
 ↓
Create file
 ↓
Read file
 ↓
Verify content
 ↓
Return success
Then test:
"Run a Node.js script that stays alive for 5 minutes."
Then:
"Send a command to the running Node process."
Then:
"Stop the process."
Only after this works should Minecraft be added.
32. Minecraft Test
Eventually:
User:
"Join my Minecraft server."
Neon should:
1. Understand request
2. Check Node.js
3. Check Mineflayer
4. Install Mineflayer if needed
5. Create bot configuration
6. Create bot script
7. Start persistent process
8. Monitor stdout/stderr
9. Connect to server
10. Verify join event
11. Keep process alive
12. Receive user commands
13. Execute actions
14. Observe results
15. Continue
This is the test that proves Neon is actually an agentic system rather than a chatbot with a command executor.
33. Development Order
Tell the coding agent to follow exactly this order:
1. README
2. Project structure
3. Configuration
4. Logging
5. Basic Python Agent
6. Tool Registry
7. Shell Tool
8. Filesystem Tool
9. Agent Loop
10. Verification System
11. Persistent Process Manager
12. Task Manager
13. llama.cpp Adapter
14. Model Router
15. Cloud Provider Adapter
16. Short-Term Memory
17. Long-Term Memory
18. RAG
19. Memory Cleanup
20. Sleep System
21. Node.js Bridge
22. MCP Manager
23. Browser Tool
24. GitHub Integration
25. Web API
26. Web UI
27. Process Dashboard
28. Memory UI
29. First persistent Node skill
30. Minecraft/Mineflayer
31. Recovery System
32. Security Hardening
33. Tests
34. Deployment
34. V1 Definition of Done
V1 should not be considered complete until this works:
User
 ↓
"Do X"
 ↓
Neon understands
 ↓
Creates plan
 ↓
Chooses tool
 ↓
Executes tool
 ↓
Observes result
 ↓
Verifies result
 ↓
If failed → recovers
 ↓
Continues
 ↓
Task completed
 ↓
Stores only useful memory
And importantly:
Never say "done" just because a command executed. Say "done" only after the requested outcome has been verified.
The first milestone
Don't build the giant system immediately.
Build this tiny vertical slice first:
Web/API
   ↓
Python Agent
   ↓
LLM
   ↓
Tool Registry
   ↓
Shell/Filesystem Tool
   ↓
Persistent Process
   ↓
Observer
   ↓
Verifier
   ↓
Result
Once that works reliably, everything else—MCP, Node.js, browser, Gemini, RAG, memory sleep, Minecraft, and the humanoid-style UI—can be layered on top without rebuilding the core.