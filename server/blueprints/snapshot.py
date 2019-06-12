from sanic.response import json
from sanic import Blueprint

from connections import get_client

snapshot_bp = Blueprint('snapshot')


@snapshot_bp.route('/list_repos')
async def list_repos(request):
    client = get_client(request)
    repos = []
    resp = await client.snapshot.get_repository()
    for repo_id, repo_type in resp.items():
        repos.append({"id": repo_id, "type": repo_type})
    return json(repos)


@snapshot_bp.route('/<repo>/list')
async def list_snaphosts(request, repo):
    client = get_client(request)
    resp = await client.snapshot.get(repo, '_all')
    return json(resp['snapshots'])
