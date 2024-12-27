from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from datetime import datetime

from DATA.const_strings import STATUS_TYPE, TOOL

@dataclass
class TimeRange:
    start: str
    end: str

@dataclass
class Feature:
    title: str
    desc: str

@dataclass
class Image:
    title: str
    desc: str
    src: Any = None  # Placeholder for image source

@dataclass
class Link:
    title: str
    href: str

@dataclass
class ProjectAttributes:
    time: TimeRange
    status: STATUS_TYPE
    tags: List[TOOL]

@dataclass
class Project:
    title: str
    description: str
    images: List[Image]
    attributes: ProjectAttributes
    features: List[Feature]
    linkDemo: Optional[Link] = None
    linkRepo: Optional[Link] = None
    linkMore: Optional[Link] = None

projects_data: List[Project] = [
    Project(
        title='DROP (patent pending)',
        description='Sole contributor to novel inventory solution using computer vision for desktop and mobile.',
        images=[],
        attributes=ProjectAttributes(
            time=TimeRange(start="May '24", end="Dec '24"),
            status=STATUS_TYPE.CLOSED,
            tags=sorted([
                TOOL.PYTHON,
                TOOL.PYTORCH,
                TOOL.FAST_API,
                TOOL.MATPLOTLIB,
                TOOL.PYDANTIC,
                TOOL.MINIO,
                TOOL.OPENCV,
                TOOL.REACT_NATIVE,
                TOOL.POSTGRES,
                TOOL.NUMPY,
            ])
        ),
        features=[
            Feature(
                title='Computer Vision',
                desc='OpenCV used for object recognition and related metric derivation.'
            ),
            Feature(
                title='Desktop & Mobile',
                desc='Cross-platform support for desktop and mobile devices.'
            ),
            Feature(
                title='Data Warehouse & API',
                desc='MinIO for object storage. Postgres for user data and licensing records.'
            ),
            Feature(
                title='Machine Learning',
                desc='PyTorch model training for enhanced object recognition'
            ),
        ],
        linkDemo=None,
        linkRepo=None,
        linkMore=None,
    ),
    Project(
        title='Tritone Analytics',
        description='Automated auditing of financial records across an arbitrary number of resources and document formats.',
        images=[],
        attributes=ProjectAttributes(
            time=TimeRange(start="Nov '23", end='Current'),
            status=STATUS_TYPE.OPEN,
            tags=sorted([
                TOOL.PANDAS,
                TOOL.FAST_API,
                TOOL.SQL_ALCH,
                TOOL.MATPLOTLIB,
                TOOL.NUMPY,
                TOOL.PYDANTIC,
                TOOL.POSTGRES,
                TOOL.MINIO,
                TOOL.GRIPTAPE_AI,
            ])
        ),
        features=[
            Feature(
                title='ETL Pipeline',
                desc='Platform migration from AWS lambda functions (python) to a self-hosted python server (FastAPI) and Postgres database'
            ),
            Feature(
                title='Data Analytics',
                desc='Replicated original functionality to regularly query Open Dental and build internal reports for owners, managers and team leads.'
            ),
            Feature(
                title='Data Warehousing',
                desc='MinIO for object storage of original documents. Postgres for parsed records, user data and generated metrics.'
            ),
            Feature(
                title='API Design',
                desc='Added API functionality for dashboard integration. Data warehouse is accesible via RESTful API for irregular report access and custom data visualization'
            ),
        ],
        linkDemo=None,
        linkRepo=None,
        linkMore=None,
    ),
]