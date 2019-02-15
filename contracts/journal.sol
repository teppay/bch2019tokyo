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

    function addDocument(address addr, string memory info) public onlyOwner {
        documents.push(addr);
        Document doc = Document(addr);
        doc.addArchive(info);
    }

    modifier onlyOwner {
        require(msg.sender == owner, "only owner");
        _;
    }

}
