pragma solidity ^0.5.1;

contract Document {
  string title;
  string [] author;
  string [] sentence;
  string [] journal;
  address owner;
  address [] publisher;
 
  function getTitle() public returns(string){
  }
 
  function getAuthor() public returns(string []){
  }
 
  function getSentence() public returns(string []){
  }
  
  function setPublisher(address addr) onlyOwner {
  }
 
  function setJournal(address addr) OnlyPublisher {
  }
 
  modifier onlyOwner {
    require(msg.sender == owner);
    _;
  }
  
  modifier OnlyPublisher {
    while(i < publisher.length){
      require(msg.sender == publisher[i]);
      i++;
    }
    _;
  }
  
}
