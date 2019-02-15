pragma solidity ^0.5.1;

contract Document {
    string title = "TITLE";
    string[] authors = ["Alice", "Bob"];
    string[] sentences = ["FUZZ_HASH1", "FUZZ_HASH2"];
    address[] journals;
    address owner;
    string[] archives;

    constructor() public {
        owner = msg.sender;
    }

    function getTitle() public view returns(string memory){
        return title;
    }

    function getNumOfAuthors() public view returns(uint){
        return authors.length;
    }

    function getAuthor(uint index) public view returns(string memory){
        return authors[index];
    }

    function getNumOfSentences() public view returns(uint){
        return sentences.length;
    }

    function getSentence(uint index) public view returns(string memory){
        return sentences[index];
    }

    function setJournal(address addr) public onlyOwner {
        journals.push(addr);
    }

    function setArchive(string memory info) public onlyJournal {
        archives.push(info);
    }

    function getNumOfArchives() public view returns(uint){
        return archives.length;
    }

    function getArchive(uint index) public view returns(string memory){
        return archives[index];
    }

    modifier onlyOwner {
        require(msg.sender == owner, "only owner");
        _;
    }

    modifier onlyJournal {
        uint i = 0;
        while(i < journals.length){
            require(msg.sender == journals[i], "only journal");
            i++;
        }
        _;
    }
}
