from typing import List, Dict, Any

from DATA.const_strings import TOOL

skill_columns: List[Dict[str, Any]] = [
    # Client
    {
        'title': 'client',
        'text': 'Client-side Tools',
        'icon': None,  # Removed React Icon component
        'skill_list': [
            TOOL.HTML_CSS.value,
            TOOL.REACT.value,
            TOOL.NEXT.value,
            TOOL.DATA_VIS.value,
            # TOOL.REACTHOOKFORM.value,
            TOOL.STYLED_COMP.value,
			TOOL.JINJA.value,
            TOOL.MUI.value,
            TOOL.CHAKRA.value,
            TOOL.REDUX.value,
            TOOL.AXIOS.value,
            # TOOL.JWT.value,
            TOOL.OAUTH.value,
            # TOOL.SAML.value,
            # TOOL.WEB_SOCKETS.value,
        ],
    },
    # Server
    {
        'title': 'server',
        'text': 'Server-side Tools',
        'icon': None,  # Removed React Icon component
        'skill_list': [
            TOOL.NODE.value,
            TOOL.EXPRESS.value,
            TOOL.FAST_API.value,
            TOOL.FASTIFY.value,
            TOOL.REST.value,
            TOOL.GRAPH_QL.value,
            TOOL.NODE_POSTGRES.value,
            TOOL.PRISMA.value,
            TOOL.UVICORN.value,
            TOOL.AWS_EC2.value,
            TOOL.AWS_LAMBDA.value,
            # TOOL.SEQUELIZE.value,
            # TOOL.CORS.value,
            # TOOL.NODEMAILER.value,
            TOOL.POSTMAN.value,
        ],
    },
    # Data
    {
        'title': 'data & ai',
        'text': 'Data Analytics...',
        'icon': None,  # Removed React Icon component
        'skill_list': [
            TOOL.PYTHON.value,
            TOOL.PANDAS.value,
            TOOL.NUMPY.value,
            TOOL.PYDANTIC.value,
			TOOL.OPENCV.value,
            TOOL.MATPLOTLIB.value,
            TOOL.SQL_ALCH.value,
            TOOL.CONDA.value,
            TOOL.LocalLLMs.value,
            TOOL.HUGGING.value,
            TOOL.AUTOGEN.value,
			TOOL.GRIPTAPE_AI.value
        ],
    },
    # Storage
    {
        'title': 'storage',
        'text': 'Database Tools',
        'icon': None,  # Removed React Icon component
        'skill_list': [
            TOOL.DB_DESIGN.value,
            TOOL.POSTGRES.value,
            TOOL.MY_SQL.value,
			TOOL.MINIO.value,
            TOOL.REDIS.value,
            TOOL.MONGO.value,
            TOOL.AWS_S3.value,
            TOOL.AWS_RDS.value,
            TOOL.SQL_SERVER.value,
            # TOOL.AWS_DYNAMO.value,
            TOOL.DB_MIGRATE.value,
        ],
    },
    # Dev Ops
    {
        'title': 'dev-ops',
        'text': 'Project Mgmt',
        'icon': None,  # Removed React Icon component
        'skill_list': [
            TOOL.GIT.value,
            TOOL.ATLASSIAN.value,
            TOOL.GIT_LAB.value,
            TOOL.DOCKER_HUB.value,
            TOOL.DOCKER_COMPOSE.value,
            # TOOL.JENKINS.value,
			TOOL.TEAM_CITY.value,
            TOOL.AGILE.value,
            TOOL.GREEN_GEEKS.value,
            TOOL.AWS_ROUTE.value,
            TOOL.AWS_PIPE.value,
            TOOL.HEROKU_PIPE.value,
            TOOL.K6.value,
            # TOOL.SCRUM.value,
            # TOOL.MOCHA.value,
        ],
    },
    # Util
    {
        'title': 'utility',
        'text': 'Other Tools...',
        'icon': None,  # Removed React Icon component
        'skill_list': [
            TOOL.LINUX.value,
            TOOL.VIM.value,
            TOOL.ZSH.value,
            TOOL.BASH.value,
            TOOL.TMUX.value,
            TOOL.YAML.value,
            TOOL.PM2.value,
            TOOL.NGROK.value,
            TOOL.OPENSSL.value,
            TOOL.SSH.value,
            # TOOL.SMTP.value,
            # TOOL.WEB_SOCKETS.value,
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