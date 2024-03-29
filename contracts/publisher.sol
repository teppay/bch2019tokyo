pragma solidity ^0.5.1;

contract Publisher {
    string organization;
    string url;
    bytes certificate;
    address owner;
    struct Journal {
        address addr;
        string title;
    }
    Journal[] journals;

    constructor(string memory _organization, string memory _url) public {
        owner = msg.sender;
        organization = _organization;
        url = _url;
    }

    function getOrganization() public view returns(string memory) {
        return organization;
    }

    function getUrl() public view returns(string memory) {
        return url;
    }

    function getCertificate() public view returns(bytes memory) {
        return certificate;
    }

    function setCertificate(bytes memory cert) public onlyOwner {
        certificate = cert;
    }

    function setOwner(address addr) public onlyOwner {
        owner = addr;
    }

    function addJournal(address addr, string memory title) public onlyOwner {
        journals.push(Journal(addr, title));
    }

    function getNumOfJournal() public view returns(uint){
        return journals.length;
    }

    function getJournalAddress(uint index) public view returns(address) {
        return journals[index].addr;
    }

    function getJournalTitle(uint index) public view returns(string memory) {
        return journals[index].title;
    }

    modifier onlyOwner {
        require(msg.sender == owner, "only owner");
        _;
    }
}
