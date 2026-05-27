from qa_toolbox.generators.user_generator import generate_user


def test_generate_user():
    user = generate_user()

    assert "email" in user
    assert "first_name" in user
    assert "last_name" in user
    assert "id" in user
    assert "phone" in user
    assert "address" in user
    assert "country" in user