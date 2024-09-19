import time

import pytest
from fastapi.testclient import TestClient

from code.server.server import app

client = TestClient(app)


@pytest.mark.asyncio
async def test_response_time():
    start_time = time.time()
    response = client.post("/message/", json={"message": "Test message"})
    assert response.status_code == 200
    end_time = time.time()
    elapsed_time = end_time - start_time
    assert elapsed_time < 0.5, f"Elapsed time {elapsed_time} exceeds 0.5 seconds"
