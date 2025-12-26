import asyncio
from tonsdk.utils import to_nano
import requests

from deploy import Deployes

async def main():
    deploy = Deployes()
    await deploy.mint_tokens()

if __name__ == "__main__":
    asyncio.run(main())