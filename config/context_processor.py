from config.settings import env_keys


def get_context_data(request):
    context = {

        "url": env_keys.get('URL'),
    }
    return context