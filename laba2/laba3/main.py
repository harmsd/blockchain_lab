import asyncio
from tonsdk.utils import to_nano
import requests

from deploy import Deployes

async def main():
    deploy = Deployes()
    await deploy.send_transfer_message(to_nano(0.01, 'ton'))


if __name__ == "__main__":
    asyncio.run(main())