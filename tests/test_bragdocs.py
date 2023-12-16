from ..services import get_service

def test_get_service():
    assert get_service.GetService() == 'I am a service'