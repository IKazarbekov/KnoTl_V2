USE_MOCK = False

if USE_MOCK:
    from .mock_user_repo import UserMockRepository as UserRepository
else:
    from .user_repo import UserRepository

user_repo = UserRepository()