from typing import List, Dict, Any

from DATA.const_strings import TOOL

skill_columns: List[Dict[str, Any]] = [
    # Client
    {
        'title': 'Client',
        'text': 'Client-side Tools',
        'icon': None,  # Removed React Icon component
        'items': [
            TOOL.HTML_CSS,
            TOOL.REACT,
            TOOL.NEXT,
            TOOL.DATA_VIS,
            # TOOL.REACTHOOKFORM,
            TOOL.STYLED_COMP,
            TOOL.MUI,
            TOOL.CHAKRA,
            TOOL.REDUX,
            TOOL.AXIOS,
            # TOOL.JWT,
            TOOL.OAUTH,
            # TOOL.SAML,
            # TOOL.WEB_SOCKETS,
        ],
    },
    # Server
    {
        'title': 'Server',
        'text': 'Server-side Tools',
        'icon': None,  # Removed React Icon component
        'items': [
            TOOL.NODE,
            TOOL.EXPRESS,
            TOOL.FAST_API,
            TOOL.FASTIFY,
            TOOL.REST,
            TOOL.GRAPH_QL,
            TOOL.AWS_EC2,
            # TOOL.AWS_LAMBDA,
            TOOL.NODE_POSTGRES,
            TOOL.PRISMA,
            TOOL.UVICORN,
            # TOOL.SEQUELIZE,
            # TOOL.CORS,
            # TOOL.NODEMAILER,
            TOOL.POSTMAN,
        ],
    },
    # Data
    {
        'title': 'Data & AI',
        'text': 'Data Analytics...',
        'icon': None,  # Removed React Icon component
        'items': [
            TOOL.PYTHON,
            TOOL.PANDAS,
            TOOL.NUMPY,
            TOOL.PYDANTIC,
            TOOL.MATPLOTLIB,
            TOOL.SQL_ALCH,
            TOOL.CONDA,
            TOOL.LocalLLMs,
            TOOL.HUGGING,
            TOOL.AUTOGEN,
        ],
    },
    # Storage
    {
        'title': 'Storage',
        'text': 'Database Tools',
        'icon': None,  # Removed React Icon component
        'items': [
            TOOL.DB_DESIGN,
            TOOL.POSTGRES,
            TOOL.AWS_S3,
            TOOL.MONGO,
            TOOL.MY_SQL,
            TOOL.SQL_SERVER,
            TOOL.REDIS,
            TOOL.AWS_RDS,
            # TOOL.AWS_DYNAMO,
            TOOL.DB_MIGRATE,
        ],
    },
    # Dev Ops
    {
        'title': 'DevOps',
        'text': 'Project Mgmt',
        'icon': None,  # Removed React Icon component
        'items': [
            TOOL.GIT,
            TOOL.ATLASSIAN,
            # TOOL.GIT_LAB,
            TOOL.DOCKER_HUB,
            TOOL.DOCKER_COMPOSE,
            # TOOL.JENKINS,
            TOOL.AGILE,
            TOOL.GREEN_GEEKS,
            TOOL.AWS_ROUTE,
            TOOL.AWS_PIPE,
            TOOL.HEROKU_PIPE,
            TOOL.K6,
            # TOOL.SCRUM,
            # TOOL.MOCHA,
        ],
    },
    # Util
    {
        'title': 'Utility',
        'text': 'Other Tools...',
        'icon': None,  # Removed React Icon component
        'items': [
            TOOL.LINUX,
            TOOL.VIM,
            TOOL.ZSH,
            TOOL.BASH,
            TOOL.TMUX,
            TOOL.YAML,
            TOOL.PM2,
            TOOL.NGROK,
            TOOL.OPENSSL,
            TOOL.SSH,
            # TOOL.SMTP,
            # TOOL.WEB_SOCKETS,
        ],
    },
]

attribute_data: List[Dict[str, Any]] = [
    {
        'heading': 'Exceedingly Curious',
        'icon': None,  # Removed React Icon component
        'description': 'Fundamentally passionate about learning and understanding systems of all kinds; digital, mechanical, societal, etc.',
        'href': '/work',
    },
    {
        'heading': 'B.S Mechanical Engineering',
        'icon': None,  # Removed React Icon component
        'description': 'Washington State University from 2006 to 2011.',
        'href': '/work',
    },
    {
        'heading': 'Project Managment',
        'icon': None,  # Removed React Icon component
        'description': 'As a co-founder of an design and fabrication company for large events. I have experience leading teams through structural fabrication and installations.',
        'href': '/work',
    },
    {
        'heading': 'Creativity',
        'icon': None,  # Removed React Icon component
        'description': "Look at the design of this website. Isn't it Unique? I made this look like this because I too am unique and cool. Hire me.",
        'href': '/work',
    },
    {
        'heading': 'Full-Stack',
        'icon': None,  # Removed React Icon component
        'description': 'I know lots of things about building web application software and my knowledge is for sale in the form of monthly payments!',
        'href': '/work',
    },
]