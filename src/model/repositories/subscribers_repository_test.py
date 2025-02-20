import pytest
from .subscribers_repository import SubscribersRepository

@pytest.mark.skip('Insert in DB')
def test_insert_subscriber():
    subscriber_infos = {
        'nome': 'Pao',
        'email': 'pao@email.com',
        'evento_id': 1
    }

    subs_repo = SubscribersRepository()
    subs_repo.insert(subscriber_infos)

@pytest.mark.skip('Select in DB')
def test_select_subscriber():
        email = 'email@email.com'
        evento_id = 1

        subs_repo = SubscribersRepository()
        resp = subs_repo.select_subscriber(email, evento_id)
        print(resp.nome)

@pytest.mark.skip('ranking link_subscriber in DB')
def test_ranking():
      evento_id = 1
      subs_repo = SubscribersRepository()
      resp  = subs_repo.get_ranking(evento_id)

      for elem in resp:
            print(f'Link: {elem.link},  total de inscritos: {elem.total}')