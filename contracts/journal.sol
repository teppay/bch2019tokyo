pragma solidity ^0.5.1;

import "./document.sol";

contract Journal {
    string title = "<Title>";
    address owner;
    address[] documents;

    constructor() public {
        owner = msg.sender;
    }

    function getTitle() public view returns(string memory) {
        return title;
    }

    function setOwner(address addr) public onlyOwner {
        owner = addr;
    }

    function setDocument(address addr, string memory info) public onlyOwner {
        documents.push(addr);
        Document doc = Document(addr);
        doc.setArchive(info);
    }

    modifier onlyOwner {
        require(msg.sender == owner, "only owner");
        _;
    }

}
