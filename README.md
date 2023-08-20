## тестовое задание hammersystem

POST api/v1/login запрос на авторизацию пользователя (phone и password)

POST api/v1/verify запрос на подтверждение 4-значного кода и авторизации (phone и verify_code)

GET api/v1/profile/<int:pk> запрос профиля конкретного пользователя 

POST api/v1/profile запрос на ввод инвайт кода (invite_code)

GET api/v1/logout выход из сессии авторизованного пользователя
