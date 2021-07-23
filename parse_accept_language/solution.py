
def parse_accept_language(clients_languages: str, server_languages: list):
    available_languages = []
    clients_languages_array = get_clients_preferences(clients_languages)
    server_languages_dict = convert_server_languages_to_dict(server_languages)
    added_languages = {}

    for client_language in clients_languages_array:
        if '-' not in client_language:
            variant_languages = get_all_serve_languages_for_language(client_language, server_languages, added_languages)
            available_languages = available_languages + variant_languages


        if client_language in server_languages_dict and client_language not in added_languages:
            added_languages[client_language] = ''
            available_languages.append(client_language)
    
    return available_languages

def convert_server_languages_to_dict(server_languages: list) -> dict:
    server_languages_dict = {}

    for language in server_languages:
        server_languages_dict[language] = ''

    return server_languages_dict


def get_clients_preferences(clients_languages):
    clients_languages_array = clients_languages.split(', ')
    return clients_languages_array


def get_all_serve_languages_for_language(language, server_languages, added_languages):
    supported_languages = []

    for server_language in server_languages:
        if language in server_language and server_language not in added_languages:
            added_languages[server_language] = ''
            supported_languages.append(server_language)


    return supported_languages