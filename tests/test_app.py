from http import HTTPStatus

from fastapi.testclient import TestClient

from curso_fast_zero.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (organizacao)

    response = client.get('/Jesus')  # Act (acao)

    assert response.status_code == HTTPStatus.OK  # 200  Assert (garanta)
    assert response.json() == {'message': 'EU sou vencedor em Cristo Jesus'}
