import os
import shutil
from git import Repo
from pygard.utils import logger

def clone_repo(repo_url, cache_dir):
    repo_path = os.path.join(cache_dir, "repo")
    if os.path.exists(repo_path):
        shutil.rmtree(repo_path)
    Repo.clone_from(repo_url, repo_path)
    logger.info(f"Repository cloned from {repo_url} to {repo_path}")
    return repo_path

def copy_policies_to_cache(repo_path, cache_dir):
    policies_src = os.path.join(repo_path, "policies")
    policies_dst = os.path.join(cache_dir, "policies")
    if os.path.exists(policies_dst):
        shutil.rmtree(policies_dst)
    shutil.copytree(policies_src, policies_dst)
    logger.info(f"Policies copied from {policies_src} to {policies_dst}")
