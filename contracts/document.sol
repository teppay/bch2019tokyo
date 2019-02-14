pragma solidity ^0.5.1;

contract Document {
  string title;
  string [] author;
  string [] sentence;
  string [] journal;
  address owner;
  address [] publisher;
 
  function getTitle() public{
  }
 
  function getAuthor() public{
  }
 
  function getSentence() public{
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
