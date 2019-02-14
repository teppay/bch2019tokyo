pragma solidity ^0.5.1;

contract Publisher {
  string Organization;
  string url;
  bytes certificates;
  string [] journal;
  mapping (address=> string) journal;
  
  function getOrganization() public returns(string) {
  }
 
  function getUrl() public returns(string) {
  }
 
  function getCertificates() public returns(bytes) {
  }
  
  function setOwner(address addr) onlyOwner {
  }
 
  function setCertificates(bytes certificates) OnlyPublisher {
  }
  
  function setJournal(address addr, string title) OnlyPublisher {
  }
 
  modifier onlyOwner {
    require(msg.sender == owner);
    _;
  }
  
}
