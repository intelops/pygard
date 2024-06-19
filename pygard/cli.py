import click
from pygard.data_model_validator import validate_data
from pygard.utils import logger, ensure_cache_dir
from pygard.git_utils import clone_repo, copy_policies_to_cache

@click.command()
@click.option('--repo_url', prompt='Git Repository URL', help='URL of the Git repository.')
@click.option('--models', prompt='Models', help='Comma-separated list of Pydantic model names.')
@click.option('--data', prompt='Data', help='JSON string of data to validate.')
def cli(repo_url, models, data):
    try:
        # Ensure cache directory exists
        cache_dir = os.path.expanduser("~/.pygard/cache")
        ensure_cache_dir(cache_dir)

        # Clone repo and copy policies
        repo_path = clone_repo(repo_url, cache_dir)
        copy_policies_to_cache(repo_path, cache_dir)

        # Validate data
        model_names = models.split(',')
        data_dict = json.loads(data)
        validation_results = validate_data(model_names, data_dict)
        click.echo(f"Validation Results: {validation_results}")
    except Exception as e:
        logger.error(f"Error: {e}")
        click.echo(f"Error: {e}")

if __name__ == '__main__':
    cli()
