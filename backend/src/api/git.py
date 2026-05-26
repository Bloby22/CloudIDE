import asyncio
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


async def git(*args: str, cwd: str | None = None) -> tuple[str, str, int]:
    proc = await asyncio.create_subprocess_exec(
        "git", *args,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        cwd=cwd,
    )
    stdout, stderr = await proc.communicate()
    return stdout.decode(errors="replace"), stderr.decode(errors="replace"), proc.returncode or 0


class CommitRequest(BaseModel):
    message: str
    cwd: str | None = None


class PushRequest(BaseModel):
    remote: str = "origin"
    branch: str = "main"
    cwd: str | None = None


class BranchRequest(BaseModel):
    name: str
    cwd: str | None = None


@router.get("/status")
async def status(cwd: str | None = None) -> dict:
    stdout, stderr, code = await git("status", "--porcelain", cwd=cwd)
    if code != 0:
        raise HTTPException(status_code=500, detail=stderr.strip())
    files = []
    for line in stdout.splitlines():
        if len(line) >= 3:
            files.append({"status": line[:2].strip(), "path": line[3:]})
    return {"files": files, "clean": len(files) == 0}


@router.get("/log")
async def log(limit: int = 20, cwd: str | None = None) -> dict:
    stdout, stderr, code = await git(
        "log", f"--max-count={limit}",
        "--pretty=format:%H|%an|%ae|%ar|%s",
        cwd=cwd,
    )
    if code != 0:
        raise HTTPException(status_code=500, detail=stderr.strip())
    commits = []
    for line in stdout.splitlines():
        parts = line.split("|", 4)
        if len(parts) == 5:
            commits.append({
                "hash": parts[0],
                "author": parts[1],
                "email": parts[2],
                "date": parts[3],
                "message": parts[4],
            })
    return {"commits": commits}


@router.post("/add")
async def add(paths: list[str], cwd: str | None = None) -> dict:
    stdout, stderr, code = await git("add", *paths, cwd=cwd)
    if code != 0:
        raise HTTPException(status_code=500, detail=stderr.strip())
    return {"ok": True}


@router.post("/commit")
async def commit(req: CommitRequest) -> dict:
    staged, _, _ = await git("diff", "--cached", "--name-only", cwd=req.cwd)
    if not staged.strip():
        raise HTTPException(status_code=400, detail="Nothing staged to commit")
    stdout, stderr, code = await git("commit", "-m", req.message, cwd=req.cwd)
    if code != 0:
        raise HTTPException(status_code=500, detail=stderr.strip())
    return {"ok": True, "output": stdout.strip()}


@router.post("/push")
async def push(req: PushRequest) -> dict:
    stdout, stderr, code = await git("push", req.remote, req.branch, cwd=req.cwd)
    if code != 0:
        raise HTTPException(status_code=500, detail=stderr.strip())
    return {"ok": True, "output": stdout.strip()}


@router.get("/branches")
async def branches(cwd: str | None = None) -> dict:
    stdout, stderr, code = await git("branch", "--list", cwd=cwd)
    if code != 0:
        raise HTTPException(status_code=500, detail=stderr.strip())
    branches_list = []
    for line in stdout.splitlines():
        active = line.startswith("*")
        branches_list.append({"name": line.lstrip("* ").strip(), "active": active})
    return {"branches": branches_list}


@router.post("/branch")
async def create_branch(req: BranchRequest) -> dict:
    _, stderr, code = await git("checkout", "-b", req.name, cwd=req.cwd)
    if code != 0:
        raise HTTPException(status_code=500, detail=stderr.strip())
    return {"ok": True, "name": req.name}


@router.get("/diff")
async def diff(path: str | None = None, cwd: str | None = None) -> dict:
    args = ["diff", path] if path else ["diff"]
    stdout, stderr, code = await git(*args, cwd=cwd)
    if code != 0:
        raise HTTPException(status_code=500, detail=stderr.strip())
    return {"diff": stdout}