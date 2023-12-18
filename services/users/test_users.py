import users

def test_create_user():
    result = users.create_user("test_first_name", "test_last_name")
    assert result == "Added User(first_name: test_first_name, 'last_name': test_last_name)"

def test_get_users():
    result = users.get_users()
    expected = [
        {
            "first_name": "test_first_name",
            "last_name": "test_last_name"
        }
    ]
    assert result == expected
    