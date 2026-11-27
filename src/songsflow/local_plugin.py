"""Local Codex stdio entrypoint with loopback-only download serving."""

import asyncio
import socket

import uvicorn

from songsflow.server import create_app, create_server


async def serve():
    # Reserve an available port before advertising URLs. Each plugin process owns
    # its own downloads; another SongsFlow instance cannot claim this listener.
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.bind(("127.0.0.1", 0))
    origin = f"http://127.0.0.1:{listener.getsockname()[1]}"
    http = uvicorn.Server(
        uvicorn.Config(create_app(origin), log_level="warning", access_log=False)
    )
    task = asyncio.create_task(http.serve(sockets=[listener]))
    try:
        while not http.started:
            if task.done():
                await task
                raise RuntimeError("SongsFlow download server could not start")
            await asyncio.sleep(0.01)
        await create_server(origin).run_async(transport="stdio", show_banner=False)
    finally:
        http.should_exit = True
        await task
        listener.close()


def main():
    asyncio.run(serve())


if __name__ == "__main__":
    main()
