pragma solidity ^0.5.1;

contract Journal {
  string title;
  address owner;
  address [] documents;
 
  function getTitle() public returns(string) {
  }

  function setOwner(address addr) onlyOwner {
  }
 
  function setDocument(address addr) OnlyPublisher {
  }
 
  modifier onlyOwner {
    require(msg.sender == owner);
    _;
  }
  
}
