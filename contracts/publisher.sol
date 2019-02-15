pragma solidity ^0.5.1;

contract Publisher {
    string organization;
    string url;
    bytes certificates;
    address owner;
    mapping (address=> string) journal;

    constructor() public {
        owner = msg.sender;
    }

    function getOrganization() public view returns(string memory) {
        return organization;
    }

    function getUrl() public view returns(string memory) {
        return url;
    }

    function getCertificates() public view returns(bytes memory) {
        return certificates;
    }

    function setOwner(address addr) public onlyOwner {
        owner = addr;
    }

    function setCertificates(bytes memory cert) public onlyOwner {
        certificates = cert;
    }

    function setJournal(address addr, string memory title) public onlyOwner {
        journal[addr] = title;
    }

    modifier onlyOwner {
        require(msg.sender == owner, "only owner");
        _;
    }
}
