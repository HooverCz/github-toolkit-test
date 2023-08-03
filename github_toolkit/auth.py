import requests
from octokit import Octokit
import json
import os

# For more details, see:
# https://docs.github.com/en/developers/apps/building-github-apps/authenticating-with-github-apps#authenticating-as-an-installation
# https://trstringer.com/github-app-authentication/


def acquire_access_token(private_key: str, app_id: str = '256305') -> str:
    """
    Function that requires private key from Github App and app id and returns ghs type access token
    Read on Github token formats: https://github.blog/2021-04-05-behind-githubs-new-authentication-token-formats/

    :param private_key: private key string or path to private key
    :param app_id: GitHub app id
    :return: ghs access token
    """
    if os.path.isfile(private_key):
        private_key_value = open(private_key, 'r').read()
    else:
        private_key_value = private_key

    # get JWT token for your installation
    octokit = Octokit(auth='app', app_id=app_id,
                      private_key=private_key_value)

    # with JWT token, get installation id
    installations = requests.get(
        f"https://api.github.com/app/installations",
        headers={'Authorization': 'Bearer %s' % octokit.jwt, 'Accept': 'application/vnd.github+json'})

    installation_id = json.loads(installations.text)[0]['id']

    # with installation id, get access token
    token = requests.post(
        f"https://api.github.com/app/installations/{installation_id}/access_tokens",
        headers={'Authorization': 'Bearer %s' % octokit.jwt, 'Accept': 'application/vnd.github+json'})

    return json.loads(token.text)['token']