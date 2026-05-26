import asyncio
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class CommandRequest(BaseModel):
    command: str
    cwd: str | None = None

class CommandResponse(BaseModel):
    stdout: str
    stderr: str
    returncode: int

@router.post("/run", response_model=CommandResponse)
async def run_command(req: CommandRequest) -> CommandResponse:
    proc = await asyncio.create_subprocess_shell(
        req.command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        cwd=req.cwd
    )
    stdout, stderr = await proc.communicate()
    return CommandResponse(
        stdout=stdout.decode(errors="replace")
        stderr=stderr.decode(errors="replace")
        returncode=proc.returncode or 0
    )