// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;
contract Transaction {
    uint _amount;
    constructor(uint amount) {
        _amount = amount;
    }
    function transaction(uint amount) public payable {
        require(address(this).balance >= amount, "not enough money");
        payable(msg.sender).transfer(amount);
    }
}