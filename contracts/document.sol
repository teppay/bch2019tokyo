pragma solidity ^0.5.1;

contract Document {
    string title;
    string authors;
    string sentences;
    address[] journal;
    address owner;
    address[] publisher;

    constructor(string memory _title, string memory _authors, string memory _sentences) public {
        owner = msg.sender;
        title = _title;
        authors = _authors;
        sentences = _sentences;
    }

    function getTitle() public view returns(string memory){
        return title;
    }

    function getAuthor() public view  returns(string memory){
        return authors;
    }

    function getSentence() public view returns(string memory){
        return sentences;
    }

    function setPublisher(address addr) public onlyOwner {
        publisher.push(addr);
    }

    function setJournal(address addr) public onlyPublisher {
        journal.push(addr);
    }

    modifier onlyOwner {
        require(msg.sender == owner, "only owner");
        _;
    }

    modifier onlyPublisher {
        uint i = 0;
        while(i < publisher.length){
            require(msg.sender == publisher[i], "only publisher");
            i++;
        }
        _;
    }
}
