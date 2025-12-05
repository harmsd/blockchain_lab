import asyncio
from tonsdk.utils import to_nano
import requests

from deploy import Deployes

async def main():
    deploy = Deployes()
    await deploy.deploy_minter()

if __name__ == "__main__":
    asyncio.run(main())