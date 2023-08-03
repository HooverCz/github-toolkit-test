import subprocess
import argparse
from github_toolkit.auth import acquire_access_token

def get_arguments():
    parser = argparse.ArgumentParser(
        description=""
    )
    parser.add_argument(
        "--private_key",
        required=True,
        metavar="private_key",
        type=str,
        help="private key string or path to private key to Github App",
    )
    parser.add_argument(
        "--app_id",
        required=True,
        metavar="app_id",
        type=str,
        help="GitHub app id",
    )
    parser.add_argument(
        "--token_name",
        required=True,
        metavar="token_name",
        type=str,
        help="Name of the token to be used",
    )
    parser.add_argument(
        "--organization",
        required=False,
        metavar="token_name",
        type=str,
        help="Name of the github organization",
        default="",
    )    
    args = parser.parse_args()
    return args.private_key, args.app_id, args.token_name, args.organization


if __name__ == '__main__':

    private_key, app_id, token_name, organization = get_arguments()

    git_token = acquire_access_token(private_key, app_id)

    bash_script = f'''
    git config --global url."https://{token_name}:{git_token}@github.com/{organization}".insteadOf "https://github.com/{organization}"
    '''

    completed_process = subprocess.run(bash_script, shell=True, check=True)

    if completed_process.returncode == 0:
        print("Git config script executed successfully.")
    else:
        print("Error executing the bash script.")
