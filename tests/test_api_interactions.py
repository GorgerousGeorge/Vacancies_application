import pytest
from unittest.mock import patch, Mock
from src.api_interactions import hh_API  # Предполагается, что ваш класс находится в файле hh_api.py


@pytest.fixture
def mock_session():
    with patch('src.api_interactions.requests.Session') as mock:
        yield mock


def test_get_vacancies(mock_session):
    hh_api_exemple = hh_API()

    mock_response = Mock()
    mock_response.json.return_value = {
        'items': [
            {
                'name': 'Python Developer',
                'alternate_url': 'https://example.com/vacancy/1',
                'salary': {'from': 1000, 'to': 2000}
            },
            {
                'name': 'Senior Python Developer',
                'alternate_url': 'https://example.com/vacancy/2',
                'salary': None
            }
        ]
    }
    mock_response.raise_for_status = Mock()
    mock_session.return_value.get.return_value = mock_response

    vacancies = hh_api_exemple.get_vacancies("Python", 10)

    assert len(vacancies) == 2
    assert vacancies[0]['name'] == 'Python Developer'
    assert vacancies[0]['salary'] == {'from': 1000, 'to': 2000}
    assert vacancies[1]['name'] == 'Senior Python Developer'
    assert vacancies[1]['salary'] is None


def test_get_vacancies_no_vacancies(mock_session):
    hh_api_exemple = hh_API()

    mock_response = Mock()
    mock_response.json.return_value = {
        'items': []
    }
    mock_response.raise_for_status = Mock()
    mock_session.return_value.get.return_value = mock_response

    vacancies = hh_api_exemple.get_vacancies("Python", 10)

    assert len(vacancies) == 0
