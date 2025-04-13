// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.26;

contract NoZeroAddressCheck {
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    modifier isOwner() {
        require(msg.sender == owner);
        _;
    }

    function setOwner(address newOwner) public isOwner {
        // missing-zero-address-validation
        owner = newOwner;
    }
}
