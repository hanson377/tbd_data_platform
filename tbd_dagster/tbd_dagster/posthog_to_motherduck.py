from typing import Any, Optional
from dagster import asset

import dlt
import os
from dlt.common.pendulum import pendulum
from dlt.sources.rest_api import (
    RESTAPIConfig,
    check_connection,
    rest_api_resources,
    rest_api_source,
)


@dlt.source(name="posthog")
def posthog_source(api_key: Optional[str] = dlt.secrets.value) -> Any:

    api_key = os.getenv('POSTHOG_API_KEY')

    # Create a REST API configuration for the PostHog API
    config: RESTAPIConfig = {
        "client": {
            "base_url": "https://us.posthog.com",
            "auth": (
                {
                    "type": "bearer",
                    "token": api_key,  # Use the provided api_key
                }
                if api_key
                else None
            ),
        },
        "resource_defaults": {
            "primary_key": "id",
            "write_disposition": "merge",
            "endpoint": {
                "params": {
                    "limit": 100,
                    "personal_api_key": api_key,  # Add the API key here
                },
            },
        },
        "resources": [
            {
                "name": "events",
                "endpoint": {
                    "path": "api/event",
                    "params": {
                        "personal_api_key": api_key,  # Use the provided api_key
                    },
                },
            },
            {
                "name": "persons",
                "endpoint": {
                    "path": "api/person",
                    "params": {
                        "personal_api_key": api_key,  # Add the API key here
                    },
                },
            },
        ],
    }

    yield from rest_api_resources(config)

@asset
def load_posthog() -> None:
    pipeline = dlt.pipeline(
        pipeline_name="rest_api_posthog",
        destination='motherduck',
        dataset_name="posthog_source",
    )

    load_info = pipeline.run(posthog_source())
    print(load_info)  # noqa: T201



if __name__ == "__main__":
    load_posthog()
