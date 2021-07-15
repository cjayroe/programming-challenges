import requests

def get_data(url) -> dict:
    response = requests.get(url)

    if response.status_code >= 300:
        raise Exception("Something went wrong calling this api")

    return response.json()


def find_user_by_name(name: str):
    users: dict = get_data('https://jsonplaceholder.typicode.com/users')

    for user in users:
        if 'name' not in user:
            continue

        user_name = user['name'].lower() 

        if name.lower() == user_name or name.lower() in user_name:
            return user
    
    return None


def get_users_posts_from_username1(name):
    user = find_user_by_name(name)

    if not user:
        raise Exception(f'Unable to find user {name}')


    posts = get_data('https://jsonplaceholder.typicode.com/posts')

    user_posts = []

    for post in posts:
        if 'userId' not in post:
            continue

        if post['userId'] == user['id']:
            user_posts.append(post)
    
    return user_posts


def get_users_posts_from_username2(name):
    user = find_user_by_name(name)

    if not user:
        raise Exception(f'Unable to find user {name}')


    user_posts = get_data(f'https://jsonplaceholder.typicode.com/users/{user["id"]}/posts')

    return user_posts