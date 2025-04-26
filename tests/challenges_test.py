import pytest
from fastapi.testclient import TestClient

from src.api import create_app


@pytest.fixture
def client():
    app = create_app()
    return TestClient(app)


@pytest.mark.parametrize(
    "input_data, output_data",
    [
        (3, 3),
        (10, 89),
        (20, 10_946),
        (50, 20_365_011_074),
    ],
)
def test_challenge_1(client, input_data: int, output_data: int):
    response = client.get(f"/challenges/solution-1?n={input_data}")

    assert response.status_code == 200
    assert response.json() == output_data


@pytest.fixture
def client():
    app = create_app()
    return TestClient(app)


@pytest.mark.parametrize(
    "input_data, output_data",
    [
        (2, 1),
        (7, 5),
        (44, 34),
        (85, 70),
    ],
)
def test_challenge_2(client, input_data: int, output_data: int):
    response = client.get(f"/challenges/solution-2?n={input_data}")

    assert response.status_code == 200
    assert response.json() == output_data


@pytest.mark.parametrize(
    "input_data, output_data",
    [
        (
            [
                [2, 0, 1],
                [0, 3, 1],
                [1, 1, 1],
            ],
            4,
        ),
        (
            [
                [1, 3, 2],
                [2, 1, 3],
                [3, 2, 1],
            ],
            9,
        ),
    ],
)
def test_challenge_3(client, input_data: int, output_data: int):
    response = client.post(
        "/challenges/solution-3",
        json=input_data
    )

    assert response.status_code == 200
    assert response.json() == output_data
