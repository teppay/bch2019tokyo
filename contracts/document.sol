pragma solidity ^0.5.1;

contract Document {
    string title;
    string[] authors;
    string[] raw_abstract;
    string[] sentences;
    string hash_function;
    address[] publishers;
    address owner;
    string[] archives;
    bool submitted = false;

    constructor(string memory _title) public {
        owner = msg.sender;
        title = _title;
    }

    modifier onlyOwner {
        require(msg.sender == owner, "only owner");
        _;
    }

    modifier onlyPublisher {
        uint i = 0;
        while(i < publishers.length){
            require(msg.sender == publishers[i], "only publisher");
            i++;
        }
        _;
    }

    modifier Submitted {
        require(submitted == false, "document submitted");
        _;
    }

    function getTitle() public view returns(string memory) {
        return title;
    }

    function setAuthor(string memory _author) public Submitted {
        authors.push(_author);
    }

    function getNumOfAuthors() public view returns(uint){
        return authors.length;
    }

    function getAuthor(uint index) public view returns(string memory){
        return authors[index];
    }

    function setAbstract(string memory _raw_abstract) public Submitted {
        raw_abstract.push(_raw_abstract);
    }

    function getNumOfAbstract() public view returns(uint){
        return raw_abstract.length;
    }

    function getAbstract(uint index) public view returns(string memory){
        return raw_abstract[index];
    }

    function setHashFunction(string memory _hash_function) public Submitted {
        hash_function = _hash_function;
    }

    function getHashFunction() public view returns(string memory) {
        return hash_function;
    }

    function setSentence(string memory _sentence) public Submitted {
        sentences.push(_sentence);
    }

    function getNumOfSentences() public view returns(uint){
        return sentences.length;
    }

    function getSentence(uint index) public view returns(string memory){
        return sentences[index];
    }

    function setPublisher(address addr) public onlyOwner {
        publishers.push(addr);
        submitted = true;
    }

    function getNumOfPublishers() public view returns(uint){
        return publishers.length;
    }

    function getPublisher(uint index) public view returns(address){
        return publishers[index];
    }

    function setArchive(string memory info) public onlyPublisher{
        archives.push(info);
    }

    function getNumOfArchives() public view returns(uint){
        return archives.length;
    }

    function getArchive(uint index) public view returns(string memory){
        return archives[index];
    }
}