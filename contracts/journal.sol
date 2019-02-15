pragma solidity ^0.5.1;

import "./document.sol";

contract Journal {
    string title;
    address owner;
    address[] documents;

    constructor(string memory _title) public {
        owner = msg.sender;
        title = _title;
    }

    function getTitle() public view returns(string memory) {
        return title;
    }

    function setOwner(address addr) public onlyOwner {
        owner = addr;
    }

    function setDocument(address addr) public onlyOwner {
        documents.push(addr);
    }

    modifier onlyOwner {
        require(msg.sender == owner, "only owner");
        _;
    }

}
