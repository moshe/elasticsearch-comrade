from sanic import Blueprint
from sanic.request import Request
from sanic.response import HTTPResponse, json

from ..connections import get_client

snapshot_bp = Blueprint('snapshot')


@snapshot_bp.route('/list_repos')
async def list_repos(request: Request) -> HTTPResponse:
    client = get_client(request)
    repos = []
    resp = await client.snapshot.get_repository()
    for repo_id, repo_type in resp.items():
        repos.append({"id": repo_id, "type": repo_type})
    return json(repos)


@snapshot_bp.route('/<repo>/list')
async def list_snaphosts(request: Request, repo: str) -> HTTPResponse:
    client = get_client(request)
    resp = await client.snapshot.get(repo, '_all')
    return json(resp['snapshots'])


@snapshot_bp.route('/create/<repo>/<snapshot>', methods=['POST'])
async def create_snaphost(request: Request, repo: str, snapshot: str) -> HTTPResponse:
    client = get_client(request)
    response = await client.snapshot.create(repo, snapshot, request.json)
    return json(response)


@snapshot_bp.route('/restore/<repo>/<snapshot>', methods=['POST'])
async def restore(request: Request, repo: str, snapshot: str) -> HTTPResponse:
    client = get_client(request)
    response = await client.snapshot.restore(repo, snapshot, request.json)
    return json(response)
