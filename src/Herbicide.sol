// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.26;

import {BaseHook, Hooks, PoolKey, IPoolManager} from "lib/v4-periphery/src/utils/BaseHook.sol";

contract HerbicideDetector is BaseHook {
    constructor(IPoolManager _manager) BaseHook(_manager) {}

    function getHookPermissions() public pure override returns (Hooks.Permissions memory) {
        return Hooks.Permissions({
            beforeInitialize: true, // SET
            afterInitialize: false,
            beforeAddLiquidity: false,
            afterAddLiquidity: false,
            beforeRemoveLiquidity: false,
            afterRemoveLiquidity: false,
            beforeSwap: true, // SET
            afterSwap: false,
            beforeDonate: false,
            afterDonate: false,
            beforeSwapReturnDelta: false,
            afterSwapReturnDelta: false,
            afterAddLiquidityReturnDelta: true,
            afterRemoveLiquidityReturnDelta: false
        });
    }

    function _beforeInitialize(address, PoolKey calldata, uint160) internal pure override returns (bytes4) {
        return this.beforeSwap.selector;
    }
}
