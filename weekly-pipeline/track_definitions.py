"""
Track definitions and seed data for the weekly Claude skills pipeline.
Each track has a list of GitHub search queries and Smithery search terms,
plus a seed list of known high-quality skills to prime the first run.
"""

TRACKS = {

    # ─────────────────────────────────────────────────────────────────────────
    # TRACK 1: Professional / Domain-Specific
    # Targets: Legal, Medical, Finance, HR, Real Estate, Insurance, etc.
    # ─────────────────────────────────────────────────────────────────────────
    "professional": {
        "label": "Professional / Domain-Specific",
        "emoji": "💼",
        "github_queries": [
            "claude subagent legal",
            "claude subagent medical healthcare",
            "claude subagent finance accounting",
            "claude subagent HR employment",
            "claude skill compliance GDPR HIPAA",
            "claude agent real estate insurance",
        ],
        "smithery_queries": [
            "legal", "medical", "finance", "compliance",
            "healthcare", "accounting", "insurance", "real estate",
        ],
        "categories": [
            "Legal", "Medical / Healthcare", "Finance", "HR / People Operations",
            "Real Estate", "Insurance", "Accounting", "Governance / Compliance",
        ],
        "seed_skills": [
            {
                "name": "contract-drafter",
                "display_name": "Contract Drafter",
                "category": "Legal",
                "description": "Draft legally sound contracts for NDAs, service agreements, employment contracts, and vendor agreements. Tailors language to jurisdiction and risk tolerance.",
                "platform_desktop": True, "platform_code": True,
                "type": "Skill",
                "source": "Seed",
            },
            {
                "name": "insurance-claim-analyst",
                "display_name": "Insurance Claim Analyst",
                "category": "Insurance",
                "description": "Analyze insurance claims for coverage applicability, identify potential fraud indicators, and draft claim response letters.",
                "platform_desktop": True, "platform_code": True,
                "type": "Skill",
                "source": "Seed",
            },
            {
                "name": "tax-advisor",
                "display_name": "Tax Advisor (US/International)",
                "category": "Finance",
                "description": "Provide tax planning guidance for individuals and businesses covering deductions, credits, estimated payments, and international tax treaties.",
                "platform_desktop": True, "platform_code": True,
                "type": "Skill",
                "source": "Seed",
            },
            {
                "name": "clinical-documentation-specialist",
                "display_name": "Clinical Documentation Specialist",
                "category": "Medical / Healthcare",
                "description": "Improve clinical documentation quality for accurate coding, reimbursement, and compliance. Covers SOAP notes, discharge summaries, and ICD-10 coding.",
                "platform_desktop": True, "platform_code": True,
                "type": "Skill",
                "source": "Seed",
            },
        ],
    },

    # ─────────────────────────────────────────────────────────────────────────
    # TRACK 2: Software Development by Language
    # Targets: Python, C#, TypeScript, Rust, Go, Java, SQL, etc.
    # ─────────────────────────────────────────────────────────────────────────
    "development": {
        "label": "Software Development by Language",
        "emoji": "💻",
        "github_queries": [
            "claude subagent python developer",
            "claude subagent csharp dotnet",
            "claude subagent typescript javascript",
            "claude subagent rust systems",
            "claude subagent golang backend",
            "claude subagent java spring",
            "claude subagent sql database",
            "claude code skill language helper",
        ],
        "smithery_queries": [
            "python", "csharp", "typescript", "rust", "golang",
            "java", "sql", "developer helper",
        ],
        "categories": [
            "Python Development", "C# / .NET Development", "TypeScript / JavaScript",
            "Rust / Systems", "Go / Backend", "Java / Spring", "SQL / Database",
            "General Dev Helpers",
        ],
        "language_priority": ["Python", "C#", "TypeScript", "Rust", "Go", "Java", "SQL"],
        "seed_skills": [
            {
                "name": "python-async-patterns",
                "display_name": "Python Async Patterns",
                "category": "Python Development",
                "description": "Master asyncio, async/await, task groups, and concurrent patterns in Python 3.11+. Covers FastAPI async endpoints, aiohttp, and async database drivers.",
                "platform_desktop": False, "platform_code": True,
                "type": "Skill",
                "source": "Seed",
            },
            {
                "name": "csharp-dotnet-architect",
                "display_name": "C# / .NET Architect",
                "category": "C# / .NET Development",
                "description": "C# and .NET 8/9 expert covering LINQ, Entity Framework Core, Dependency Injection, Minimal APIs, Blazor, and Clean Architecture patterns.",
                "platform_desktop": False, "platform_code": True,
                "type": "Skill",
                "source": "Seed",
            },
            {
                "name": "typescript-type-wizard",
                "display_name": "TypeScript Type Wizard",
                "category": "TypeScript / JavaScript",
                "description": "Advanced TypeScript type system expert covering conditional types, mapped types, template literal types, discriminated unions, and type-safe API design.",
                "platform_desktop": False, "platform_code": True,
                "type": "Skill",
                "source": "Seed",
            },
            {
                "name": "rust-memory-safety",
                "display_name": "Rust Memory Safety Expert",
                "category": "Rust / Systems",
                "description": "Rust ownership, borrowing, lifetimes, async Tokio, and systems programming patterns. Covers WebAssembly, embedded Rust, and performance-critical applications.",
                "platform_desktop": False, "platform_code": True,
                "type": "Skill",
                "source": "Seed",
            },
            {
                "name": "sql-query-optimizer",
                "display_name": "SQL Query Optimizer",
                "category": "SQL / Database",
                "description": "SQL query optimization expert covering execution plans, index strategies, window functions, CTEs, and database-specific tuning for PostgreSQL, MySQL, and SQL Server.",
                "platform_desktop": False, "platform_code": True,
                "type": "Skill",
                "source": "Seed",
            },
        ],
    },

    # ─────────────────────────────────────────────────────────────────────────
    # TRACK 3: Everyday Household / Busy Family
    # Targets: Meal planning, budgeting, scheduling, home maintenance,
    #          parenting, homework help, travel, health & wellness, etc.
    # ─────────────────────────────────────────────────────────────────────────
    "household": {
        "label": "Everyday Household / Busy Family",
        "emoji": "🏠",
        "github_queries": [
            "claude skill meal planning family",
            "claude skill home budget personal finance",
            "claude skill parenting homework help",
            "claude skill travel planning vacation",
            "claude skill home maintenance repair",
            "claude skill health wellness everyday",
            "claude skill grocery shopping list",
        ],
        "smithery_queries": [
            "meal planning", "family budget", "homework", "travel",
            "home maintenance", "wellness", "grocery", "parenting",
        ],
        "categories": [
            "Meal Planning & Nutrition", "Family Budgeting", "Parenting & Education",
            "Travel Planning", "Home Maintenance", "Health & Wellness",
            "Shopping & Errands", "Personal Productivity",
        ],
        "seed_skills": [
            {
                "name": "weekly-meal-planner",
                "display_name": "Weekly Meal Planner",
                "category": "Meal Planning & Nutrition",
                "description": "Create personalized weekly meal plans based on dietary preferences, allergies, family size, and budget. Generates shopping lists, prep schedules, and nutritional summaries.",
                "platform_desktop": True, "platform_code": True,
                "type": "Skill",
                "source": "Seed",
            },
            {
                "name": "family-budget-tracker",
                "display_name": "Family Budget Tracker",
                "category": "Family Budgeting",
                "description": "Analyze household income and expenses, identify savings opportunities, create monthly budgets, and provide actionable tips to reduce spending without sacrificing quality of life.",
                "platform_desktop": True, "platform_code": True,
                "type": "Skill",
                "source": "Seed",
            },
            {
                "name": "homework-helper",
                "display_name": "Homework Helper (K-12)",
                "category": "Parenting & Education",
                "description": "Patient, grade-appropriate homework assistance covering math, science, history, English, and foreign languages. Explains concepts step-by-step and encourages independent thinking.",
                "platform_desktop": True, "platform_code": True,
                "type": "Skill",
                "source": "Seed",
            },
            {
                "name": "family-vacation-planner",
                "display_name": "Family Vacation Planner",
                "category": "Travel Planning",
                "description": "Plan family-friendly vacations with itineraries, accommodation recommendations, activity suggestions for all ages, packing lists, and budget breakdowns.",
                "platform_desktop": True, "platform_code": True,
                "type": "Skill",
                "source": "Seed",
            },
            {
                "name": "home-maintenance-advisor",
                "display_name": "Home Maintenance Advisor",
                "category": "Home Maintenance",
                "description": "Seasonal home maintenance checklists, DIY repair guidance, contractor hiring tips, and home improvement project planning to protect your investment.",
                "platform_desktop": True, "platform_code": True,
                "type": "Skill",
                "source": "Seed",
            },
            {
                "name": "wellness-coach",
                "display_name": "Everyday Wellness Coach",
                "category": "Health & Wellness",
                "description": "Personalized wellness guidance covering sleep hygiene, stress management, exercise routines for busy schedules, and healthy habit formation for the whole family.",
                "platform_desktop": True, "platform_code": True,
                "type": "Skill",
                "source": "Seed",
            },
            {
                "name": "grocery-list-optimizer",
                "display_name": "Grocery List Optimizer",
                "category": "Shopping & Errands",
                "description": "Optimize grocery shopping by organizing lists by store section, identifying sales and coupons, suggesting store-brand substitutions, and minimizing food waste.",
                "platform_desktop": True, "platform_code": True,
                "type": "Skill",
                "source": "Seed",
            },
            {
                "name": "family-scheduler",
                "display_name": "Family Scheduler & Coordinator",
                "category": "Personal Productivity",
                "description": "Coordinate complex family schedules including school events, sports, appointments, and work commitments. Identifies conflicts, suggests solutions, and creates shared calendar summaries.",
                "platform_desktop": True, "platform_code": True,
                "type": "Skill",
                "source": "Seed",
            },
            {
                "name": "college-application-coach",
                "display_name": "College Application Coach",
                "category": "Parenting & Education",
                "description": "Guide high school students through the college application process covering essay writing, school selection, financial aid, scholarship research, and interview preparation.",
                "platform_desktop": True, "platform_code": True,
                "type": "Skill",
                "source": "Seed",
            },
            {
                "name": "pet-care-advisor",
                "display_name": "Pet Care Advisor",
                "category": "Health & Wellness",
                "description": "Practical pet care guidance covering nutrition, training, health monitoring, vet visit preparation, and behavioral issues for dogs, cats, and common household pets.",
                "platform_desktop": True, "platform_code": True,
                "type": "Skill",
                "source": "Seed",
            },
        ],
    },

    # ─────────────────────────────────────────────────────────────────────────
    # TRACK 4: New Claude Features / Hooks
    # Targets: New Claude Desktop/Code features, MCP hooks, tool use patterns,
    #          agentic workflows, Claude.ai new capabilities, etc.
    # ─────────────────────────────────────────────────────────────────────────
    "claude_features": {
        "label": "New Claude Features & Hooks",
        "emoji": "🤖",
        "github_queries": [
            "claude code hooks lifecycle",
            "claude MCP server new 2026",
            "claude desktop skill new feature",
            "claude agent tool use pattern",
            "claude subagent orchestration pattern",
            "claude code memory context",
            "claude computer use automation",
        ],
        "smithery_queries": [
            "hooks", "lifecycle", "orchestration", "computer use",
            "memory", "tool use", "MCP", "automation",
        ],
        "categories": [
            "Claude Code Hooks", "MCP Servers & Integrations",
            "Computer Use / Browser Automation", "Memory & Context Management",
            "Multi-Agent Orchestration", "Claude Desktop Features",
            "Tool Use Patterns", "Agentic Workflows",
        ],
        "seed_skills": [
            {
                "name": "pre-tool-use-hook",
                "display_name": "Pre-Tool-Use Safety Hook",
                "category": "Claude Code Hooks",
                "description": "Intercepts all tool use calls before execution to validate inputs, enforce safety policies, log actions, and prevent destructive operations. Uses Claude Code's lifecycle hooks system.",
                "platform_desktop": False, "platform_code": True,
                "type": "Hook / Skill",
                "source": "Seed",
            },
            {
                "name": "post-tool-use-auditor",
                "display_name": "Post-Tool-Use Auditor",
                "category": "Claude Code Hooks",
                "description": "Captures and logs all tool use results after execution for audit trails, debugging, and compliance reporting. Generates structured JSON audit logs per session.",
                "platform_desktop": False, "platform_code": True,
                "type": "Hook / Skill",
                "source": "Seed",
            },
            {
                "name": "computer-use-navigator",
                "display_name": "Computer Use Navigator",
                "category": "Computer Use / Browser Automation",
                "description": "Automate desktop and browser tasks using Claude's computer use capability. Covers form filling, data extraction, UI testing, and repetitive desktop workflows.",
                "platform_desktop": True, "platform_code": True,
                "type": "Skill",
                "source": "Seed",
            },
            {
                "name": "mcp-filesystem-manager",
                "display_name": "MCP Filesystem Manager",
                "category": "MCP Servers & Integrations",
                "description": "Manage local files and directories through Claude Desktop using the MCP filesystem server. Covers file search, bulk rename, content extraction, and directory organization.",
                "platform_desktop": True, "platform_code": False,
                "type": "Skill (MCP)",
                "source": "Seed",
            },
            {
                "name": "session-memory-manager",
                "display_name": "Session Memory Manager",
                "category": "Memory & Context Management",
                "description": "Persist and recall important context across Claude Code sessions using structured memory files. Covers entity tracking, decision logging, and context summarization.",
                "platform_desktop": False, "platform_code": True,
                "type": "Skill",
                "source": "Seed",
            },
            {
                "name": "parallel-research-orchestrator",
                "display_name": "Parallel Research Orchestrator",
                "category": "Multi-Agent Orchestration",
                "description": "Spawn multiple research sub-agents in parallel to investigate different aspects of a topic simultaneously, then synthesize their findings into a unified report.",
                "platform_desktop": False, "platform_code": True,
                "type": "Orchestrator",
                "source": "Seed",
            },
        ],
    },
}

# Top 10 Household / Everyday Helper Skills (standalone list for immediate use)
TOP_10_HOUSEHOLD = [
    "weekly-meal-planner",
    "family-budget-tracker",
    "homework-helper",
    "family-vacation-planner",
    "home-maintenance-advisor",
    "wellness-coach",
    "grocery-list-optimizer",
    "family-scheduler",
    "college-application-coach",
    "pet-care-advisor",
]

# Top 10 New Claude Features / Hooks
TOP_10_CLAUDE_FEATURES = [
    "pre-tool-use-hook",
    "post-tool-use-auditor",
    "computer-use-navigator",
    "mcp-filesystem-manager",
    "session-memory-manager",
    "parallel-research-orchestrator",
    "pensyve-cross-session-memory",
    "mcp-policy-enforcer",
    "agent-identifier-router",
    "claude-code-tdd-workflow",
]
