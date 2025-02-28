#  See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from livewrapped_sdk import LivewrappedSDK, AsyncLivewrappedSDK
from livewrapped_sdk.types.stats_inventory.sites import AdUnitListResponse, AdUnitRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdUnits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: LivewrappedSDK) -> None:
        ad_unit = client.stats_inventory.sites.ad_units.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AdUnitRetrieveResponse, ad_unit, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LivewrappedSDK) -> None:
        response = client.stats_inventory.sites.ad_units.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_unit = response.parse()
        assert_matches_type(AdUnitRetrieveResponse, ad_unit, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LivewrappedSDK) -> None:
        with client.stats_inventory.sites.ad_units.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_unit = response.parse()
            assert_matches_type(AdUnitRetrieveResponse, ad_unit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: LivewrappedSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            client.stats_inventory.sites.ad_units.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: LivewrappedSDK) -> None:
        ad_unit = client.stats_inventory.sites.ad_units.list()
        assert_matches_type(AdUnitListResponse, ad_unit, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: LivewrappedSDK) -> None:
        response = client.stats_inventory.sites.ad_units.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_unit = response.parse()
        assert_matches_type(AdUnitListResponse, ad_unit, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: LivewrappedSDK) -> None:
        with client.stats_inventory.sites.ad_units.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_unit = response.parse()
            assert_matches_type(AdUnitListResponse, ad_unit, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAdUnits:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLivewrappedSDK) -> None:
        ad_unit = await async_client.stats_inventory.sites.ad_units.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AdUnitRetrieveResponse, ad_unit, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLivewrappedSDK) -> None:
        response = await async_client.stats_inventory.sites.ad_units.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_unit = await response.parse()
        assert_matches_type(AdUnitRetrieveResponse, ad_unit, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLivewrappedSDK) -> None:
        async with async_client.stats_inventory.sites.ad_units.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_unit = await response.parse()
            assert_matches_type(AdUnitRetrieveResponse, ad_unit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLivewrappedSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            await async_client.stats_inventory.sites.ad_units.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLivewrappedSDK) -> None:
        ad_unit = await async_client.stats_inventory.sites.ad_units.list()
        assert_matches_type(AdUnitListResponse, ad_unit, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLivewrappedSDK) -> None:
        response = await async_client.stats_inventory.sites.ad_units.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_unit = await response.parse()
        assert_matches_type(AdUnitListResponse, ad_unit, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLivewrappedSDK) -> None:
        async with async_client.stats_inventory.sites.ad_units.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_unit = await response.parse()
            assert_matches_type(AdUnitListResponse, ad_unit, path=["response"])

        assert cast(Any, response.is_closed) is True
