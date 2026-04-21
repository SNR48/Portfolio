from django.shortcuts import render


def index(request):
    context = {
        "name": "Sivanagaraju Naradala",
        "title": "Data Scientist & GenAI Engineer",
        "tagline": "Building intelligent systems at the intersection of ML, LLMs, and production AI systems.",
        "email": "sivanagarajudreams@gmail.com",
        "phone": "07981578718",
        "location": "Hyderabad, India",
        "linkedin": "https://linkedin.com/in/sivanagaraju-naradala-0637a0217",
        "summary": (
            "Data Scientist and GenAI Engineer with 4+ years of experience delivering scalable "
            "machine learning, predictive analytics, and LLM-powered solutions. Focused on "
            "end-to-end ML pipelines, RAG-based conversational AI, and production deployment "
            "on Google Cloud."
        ),
        "profile_image": "images/Siva.jpg",
        "profile_focus": [
            "RAG Systems",
            "LLM Apps",
            "FastAPI APIs",
            "Google Cloud",
        ],
        "profile_experience": [
            {
                "label": "GenAI Engineer",
                "detail": "RAG chatbots, embeddings, vector search, semantic retrieval",
            },
            {
                "label": "Data Scientist",
                "detail": "Predictive modeling, analytics pipelines, real-time insights",
            },
        ],
        "skills": [
            {
                "category": "Programming & Tools",
                "icon": "⚙️",
                "items": [
                    {"logo": "https://skillicons.dev/icons?i=python", "name": "Python"},
                    {"logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg", "name": "OOP"},
                    {"logo": "https://skillicons.dev/icons?i=git", "name": "Git"},
                    {"logo": "https://skillicons.dev/icons?i=fastapi", "name": "FastAPI"},
                    {"logo": "https://skillicons.dev/icons?i=gcp", "name": "Google Cloud"},
                    {"logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jira/jira-original.svg", "name": "Agile/Scrum"},
                ],
            },
            {
                "category": "Data Analysis",
                "icon": "📊",
                "items": [
                    {"logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg", "name": "Pandas"},
                    {"logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg", "name": "NumPy"},
                    {"logo": "https://skillicons.dev/icons?i=postgres", "name": "EDA"},
                    {"logo": "https://skillicons.dev/icons?i=sklearn", "name": "Feature Engineering"},
                    {"logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/matplotlib/matplotlib-original.svg", "name": "Matplotlib"},
                    {"logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg", "name": "Seaborn"},
                ],
            },
            {
                "category": "Machine Learning",
                "icon": "🤖",
                "items": [
                    {"logo": "https://skillicons.dev/icons?i=sklearn", "name": "Classification"},
                    {"logo": "https://skillicons.dev/icons?i=sklearn", "name": "Regression"},
                    {"logo": "https://skillicons.dev/icons?i=sklearn", "name": "Clustering"},
                    {"logo": "https://skillicons.dev/icons?i=tensorflow", "name": "Ensemble Models"},
                    {"logo": "https://skillicons.dev/icons?i=anaconda", "name": "Hyperparameter Tuning"},
                ],
            },
            {
                "category": "NLP & Deep Learning",
                "icon": "🧠",
                "items": [
                    {"logo": "https://skillicons.dev/icons?i=tensorflow", "name": "NLP"},
                    {"logo": "https://skillicons.dev/icons?i=pytorch", "name": "Transformers"},
                    {"logo": "https://huggingface.co/front/assets/huggingface_logo-noborder.svg", "name": "Hugging Face"},
                    {"logo": "https://skillicons.dev/icons?i=pytorch", "name": "Embeddings"},
                ],
            },
            {
                "category": "LLM & GenAI",
                "icon": "✨",
                "items": [
                    {"logo": "https://skillicons.dev/icons?i=ai", "name": "LLMs"},
                    {"logo": "https://skillicons.dev/icons?i=elasticsearch", "name": "RAG"},
                    {"logo": "https://registry.npmmirror.com/@lobehub/icons-static-png/latest/files/light/langchain-color.png", "name": "LangChain"},
                    {"logo": "https://skillicons.dev/icons?i=elasticsearch", "name": "Vector Databases"},
                    {"logo": "https://skillicons.dev/icons?i=latex", "name": "Prompt Tuning"},
                ],
            },
            {
                "category": "Databases",
                "icon": "🗄️",
                "items": [
                    {"logo": "https://skillicons.dev/icons?i=mysql", "name": "MySQL"},
                    {"logo": "https://skillicons.dev/icons?i=postgres", "name": "SQL"},
                    {"logo": "https://cdn.brandfetch.io/idnJwqY4I2/theme/dark/logo.svg?c=1dxbfHSJFAPEGdCLU4o5B", "name": "FAISS"},
                    {"logo": "https://avatars.githubusercontent.com/u/106068485?s=200&v=4", "name": "ChromaDB"},
                ],
            },
        ],
        "experiences": [
            {
                "company": "Keerraan Techno Analysis Pvt Ltd",
                "duration": "Oct 2021 - Present",
                "role": "GenAI Engineer",
                "project": "RAG-Based Conversational AI",
                "color": "cyan",
                "points": [
                    "Designed and implemented an end-to-end RAG chatbot for context-aware answers and automated test case generation for fleet management.",
                    "Built document ingestion pipelines for PDF and Excel sources, including extraction, preprocessing, chunking, and semantic embeddings.",
                    "Integrated LangChain, FAISS/Chroma, and LLMs for scalable semantic search and grounded responses.",
                    "Developed and deployed asynchronous REST APIs using FastAPI.",
                ],
            },
            {
                "company": "Keerraan Techno Analysis Pvt Ltd",
                "duration": "Oct 2021 - Present",
                "role": "Data Scientist",
                "project": "Vehicle Data Analysis",
                "color": "green",
                "points": [
                    "Designed end-to-end vehicle analytics pipelines using SQL and Python for large-scale sensor and trip datasets.",
                    "Engineered domain-specific features such as fuel efficiency, idle ratio, engine load, and trip-level metrics.",
                    "Built regression and classification models for fuel consumption analysis and maintenance prediction.",
                    "Hosted production services on Google Cloud Compute Engine with reliable request handling.",
                ],
            },
        ],
        "education": {
            "degree": "Bachelor of Technology - Computer Science Engineering",
            "college": "Vikas College of Engineering and Technology, JNTUK",
            "score": "78%",
        },
        "certification": {
            "title": "AI-ML Internship",
            "org": "Try Logic Soft Solutions",
            "duration": "6 Months",
        },
        "languages": [
            {"name": "Telugu", "level": "Native / Bilingual"},
            {"name": "English", "level": "Fluent"},
        ],
    }
    return render(request, "portfolio/index.html", context)
