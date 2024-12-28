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
                TOOL.PYTHON.value,
                TOOL.PYTORCH.value,
                TOOL.FAST_API.value,
                TOOL.MATPLOTLIB.value,
                TOOL.PYDANTIC.value,
                TOOL.MINIO.value,
                TOOL.OPENCV.value,
                TOOL.REACT_NATIVE.value,
                TOOL.POSTGRES.value,
                TOOL.NUMPY.value,
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
                TOOL.PANDAS.value,
                TOOL.FAST_API.value,
                TOOL.SQL_ALCH.value,
                TOOL.MATPLOTLIB.value,
                TOOL.NUMPY.value,
                TOOL.PYDANTIC.value,
                TOOL.POSTGRES.value,
                TOOL.MINIO.value,
                TOOL.GRIPTAPE_AI.value,
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