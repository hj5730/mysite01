from user import models

def test_models_insert():
    models.insert('마이콜', 'michol@naver.com', '1234', 'male')

def test_models_findby_email_and_password():
    result = models.findby_email_and_password('michol@naver.com', '1234')
    print(result)

# test_models_insert()
test_models_findby_email_and_password()