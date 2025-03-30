import pytest
from unittest.mock import patch, Mock
from src.vacancies import Vacancy


@pytest.fixture
def mock_session():
    with patch('src.api_interactions.requests.Session') as mock:
        yield mock


@pytest.fixture
def vacancy1():
    return Vacancy('Python Developer', 'Pupa Company', 100000, "некорректная ссылка")


@pytest.fixture
def vacancy2():
    return Vacancy('Senior Python Developer', 'Lupa Enterprise', -200000, "http://example.com")


@pytest.fixture
def vacancy3():
    return Vacancy('SRE engineer', 200000, 200000, "http://example.com")


@pytest.fixture
def vacancy4():
    return Vacancy(4, 'Trulyalya Official', 150000, "http://example.com")


@pytest.fixture
def vacancy5():
    return Vacancy('Data Analyst', 'Tralyalya Incorporated', 150000, "http://example.com")
