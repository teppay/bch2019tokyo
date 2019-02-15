pragma solidity ^0.5.1;

contract Document {
    string title;
    string[] authors;
    string[] sentences;
    address[] journals;
    address owner;
    string[] archives;
    bool enclosed = false;

    constructor(string memory _title) public {
        owner = msg.sender;
        title = _title;
    }

    function getTitle() public view returns(string memory) {
        return title;
    }

    function addAuthor(string memory _author) public ownerUnenclosed {
        authors.push(_author);
    }

    function getNumOfAuthors() public view returns(uint){
        return authors.length;
    }

    function getAuthor(uint index) public view returns(string memory){
        return authors[index];
    }

    function addSentences(string memory _sentence) public ownerUnenclosed {
        sentences.push(_sentence);
    }

    function getNumOfSentences() public view returns(uint){
        return sentences.length;
    }

    function getSentence(uint index) public view returns(string memory){
        return sentences[index];
    }

    function addJournal(address addr) public onlyOwner {
        journals.push(addr);
        enclosed = true;
    }

    function addArchive(string memory info) public onlyJournal {
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

    modifier ownerUnenclosed {
        require(enclosed == false, "owner enclosed");
        _;
    }
}
